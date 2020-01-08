from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

while True:
    GPIO.output(8, GPIO.HIGH)
    sleep(5)
    GPIO.output(8, GPIO.LOW)
    sleep(5)
