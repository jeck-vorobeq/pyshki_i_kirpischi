import time

import controller
import modul
import view

while True:
    time.sleep(1/120)
    modul.all_modul()
    view.draw()
    controller.joystick()
