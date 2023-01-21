import time

import controller
import modul
import view

while True:
    time.sleep(1/120)
    view.draw()
    controller.joystick()
    modul.all_modul()