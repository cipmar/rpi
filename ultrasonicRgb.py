import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

trigPin = 16
echoPin = 18
redLedPin = 8
greenLedPin = 10
blueLedPin = 12

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(redLedPin, GPIO.OUT)
GPIO.setup(greenLedPin, GPIO.OUT)
GPIO.setup(blueLedPin, GPIO.OUT)

def calculate_distance(): # in cm
    GPIO.output(trigPin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trigPin, GPIO.LOW)

    start = time.time()
    stop = time.time()

    while GPIO.input(echoPin) == 0:
        start = time.time()

    while GPIO.input(echoPin) == 1:
        stop = time.time()

    duration = stop - start
    soundSpeed = 34300 # in cm/s
    distance = soundSpeed * duration / 2

    return distance

try:
    while True:
        distance = calculate_distance()
        print("Distance: %.2f cm" % distance)
        
        if distance < 25:
            GPIO.output(redLedPin, GPIO.HIGH)
            GPIO.output(greenLedPin, GPIO.LOW)
            time.sleep(0.1)

        else:
            GPIO.output(greenLedPin, GPIO.HIGH)
            GPIO.output(redLedPin, GPIO.LOW)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
