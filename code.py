# MouseShake
import time
import board
import digitalio
import usb_hid
from adafruit_hid.mouse import Mouse

max_shake_minutes = 240
move_distance = 100
mouse_pause = .5

led = digitalio.DigitalInOut(board.GP14)
led.direction = digitalio.Direction.OUTPUT
button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)
mouse = Mouse(usb_hid.devices)

active_state = False;
active_time = 0;
led.value = False

while True:
    if button.value:
        active_state = not active_state
        if active_state:
            led.value = True
            active_time = time.time()
        else:
            led.value = False
    if active_state:
        mouse.move(x=move_distance)
        time.sleep(mouse_pause)
        mouse.move(x=-1 * move_distance)
        time.sleep(mouse_pause)
        elapsed = time.time()- active_time
        if elapsed >= (max_shake_minutes * 60):
            active_state = False
            active_time = 0
            led.value = False
    else:
        time.sleep(0.5)
        
#    print(active_state)
#    print(active_time)
#    if active_state:
#        print(time.time()- active_time)


