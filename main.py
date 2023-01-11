import eel
import pyowm

owm = pyowm.OWM("6d00d1d4e704068d70191bad2673e0cc")

@eel.expose
def get_w(place):
   
    mgr = owm.weather_manager()
    obs = mgr.weather_at_place(place)
    w = obs.weather

    temp = w.temperature('celsius')['temp']

    return "в городе " + place + "сейчас " + str(temp) + " градусов!"


eel.init("web")
eel.start("main.html", size =(700, 700))