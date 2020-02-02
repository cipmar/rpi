import pigpio
import time

# define pins in BCM mode
led = 14 # pin 8 in BOARD mode
buttonOn = 24 # pin 18 in BOARD mode
buttonOff = 8 # pin 24 in BOARD mode

pi = pigpio.pi()
pi.set_mode(led, pigpio.OUTPUT)
pi.set_pull_up_down(buttonOn, pigpio.PUD_UP)
pi.set_pull_up_down(buttonOff, pigpio.PUD_UP)

buttonOnPressed = False
buttonOffPressed = False

try:
    while True:
        # check if buttonOn was pressed
        if pi.read(buttonOn) == 0 and not buttonOnPressed:
                print("buttonOn pressed")
                pi.write(led, 1) # turn on the led
                buttonOnPressed = True
                buttonOffPressed = False

        if pi.read(buttonOff) == 0 and not buttonOffPressed:
            print("buttonOff pressed")
            pi.write(led, 0) # turn off the led
            buttonOffPressed = True
            buttonOnPressed = False

        time.sleep(0.01)
except KeyboardInterrupt:
    pass

pi.stop()
