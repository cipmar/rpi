import pigpio
import time

# define pins in BCM mode
led = 14 # pin 8 in BOARD mode
buttonUp = 24 # pin 18 in BOARD mode
buttonDown = 8 # pin 24 in BOARD mode

pi = pigpio.pi()
pi.set_mode(led, pigpio.OUTPUT)
pi.set_pull_up_down(buttonUp, pigpio.PUD_UP)
pi.set_pull_up_down(buttonDown, pigpio.PUD_UP)

dutyCycle = 0
try:
    while True:
        while pi.read(buttonDown) == 0:
            if dutyCycle > 1:
                dutyCycle = dutyCycle - 1
            else:
                dutyCycle = 0

            pi.set_PWM_dutycycle(led, dutyCycle)
            time.sleep(0.05)

        while pi.read(buttonUp) == 0:
            if dutyCycle < 100:
                dutyCycle = dutyCycle + 1
            else:
                dutyCycle = 100

            pi.set_PWM_dutycycle(led, dutyCycle)
            time.sleep(0.05)
except KeyboardInterrupt:
    pass

pi.stop()
