from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

try:
    while True:
        GPIO.output(8, GPIO.HIGH)
        sleep(1)
        GPIO.output(8, GPIO.LOW)

        GPIO.output(10, GPIO.HIGH)
        sleep(1)
        GPIO.output(10, GPIO.LOW)

        GPIO.output(12, GPIO.HIGH)
        sleep(1)
        GPIO.output(12, GPIO.LOW)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
