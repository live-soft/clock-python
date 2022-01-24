import eel
import datetime
import threading

eel.init("web")

@eel.expose()
def setInterval():
    e = threading.Event()
    while not e.wait(1):
        dateTime = datetime.datetime.now()

        hours = int(dateTime.strftime('%H'))
        minutes =int(dateTime.strftime('%M'))
        seconds = int(dateTime.strftime('%S'))

        eel.clock(seconds * 6, (minutes * 6) + (seconds / 10), (hours) * 30 + (minutes / 2) + (seconds / 2 / 60))

eel.start("index.html", size = (600, 600))