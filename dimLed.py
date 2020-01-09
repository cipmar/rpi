from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.OUT)

pwmPIN = GPIO.PWM(8, 1000)

pwmPIN.start(0)

try:
    while True:
        for i in range(100):
            pwmPIN.ChangeDutyCycle(i)
            sleep(0.01)

        for i in reversed(range(100)):
            pwmPIN.ChangeDutyCycle(i)
            sleep(0.01)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
