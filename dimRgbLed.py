from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

redPWM = GPIO.PWM(8, 1000)
greenPWM = GPIO.PWM(10, 1000)
bluePWM = GPIO.PWM(12, 1000)

redPWM.start(0)
greenPWM.start(0)
bluePWM.start(0)

def single(ledPin):
    for i in range(100):
        ledPin.ChangeDutyCycle(i)
        sleep(0.01)

    for i in reversed(range(100)):
        ledPin.ChangeDutyCycle(i)
        sleep(0.01)

def duo(firstLed, secondLed):
    for i in range(100):
        firstLed.ChangeDutyCycle(i)
        secondLed.ChangeDutyCycle(i)
        sleep(0.01)

    for i in reversed(range(100)):
        firstLed.ChangeDutyCycle(i)
        secondLed.ChangeDutyCycle(i)
        sleep(0.01)

def all(firstLed, secondLed, thirdLed):
    for i in range(100):
        firstLed.ChangeDutyCycle(i)
        secondLed.ChangeDutyCycle(i)
        thirdLed.ChangeDutyCycle(i)
        sleep(0.01)

    for i in reversed(range(100)):
        firstLed.ChangeDutyCycle(i)
        secondLed.ChangeDutyCycle(i)
        thirdLed.ChangeDutyCycle(i)
        sleep(0.01)

try:
    while True:
        single(redPWM)
        single(bluePWM)
        single(greenPWM)
        duo(redPWM, bluePWM)
        duo(redPWM, greenPWM)
        duo(bluePWM, greenPWM)
        all(bluePWM, redPWM, greenPWM)
except KeyboardInterrupt:
    pass

GPIO.cleanup()

