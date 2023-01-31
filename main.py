import time

import controller
import view
import modul

while True:
    time.sleep(1/120)
    modul.all_modul()
    view.draw()
    controller.joystick()
