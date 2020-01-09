from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

# pin to control the speed of the motor
speedPin = 8

# pins to control the direction of the motor
dirAPin = 10
dirBPin = 22

# time to stay on (seconds)
delayOn = 3

# time to stay off (seconds)
delayOff = 1.5

GPIO.setup(speedPin, GPIO.OUT)
GPIO.setup(dirAPin, GPIO.OUT)
GPIO.setup(dirBPin, GPIO.OUT)

pwmSpeedPin = GPIO.PWM(speedPin, 100)
pwmSpeedPin.start(0)

def turnOff():
    pwmSpeedPin.ChangeDutyCycle(0)
    GPIO.output(dirAPin, GPIO.LOW)
    GPIO.output(dirBPin, GPIO.LOW)
    sleep(delayOff)

def turnOn(speed, dirPin, notDirPin):
    pwmSpeedPin.ChangeDutyCycle(speed)
    GPIO.output(dirPin, GPIO.HIGH)
    GPIO.output(notDirPin, GPIO.LOW)
    sleep(delayOn)
    turnOff()

try:
    while True:
        # motor full, turn in one direction
        turnOn(100, dirAPin, dirBPin);
        
        # motor full, turn in opossite direction
        turnOn(100, dirBPin, dirAPin);

        # motor 50% speed, turn in one direction
        turnOn(50, dirAPin, dirBPin);
        
        # motor 50% speed, turn in opposite direction
        turnOn(50, dirBPin, dirAPin)

        # motor 0 to 100 speed
        GPIO.output(dirAPin, GPIO.HIGH)
        GPIO.output(dirBPin, GPIO.LOW)

        for i in range(100):
            pwmSpeedPin.ChangeDutyCycle(i)
            sleep(0.2)
        
        turnOff()


except KeyboardInterrupt:
    pass

GPIO.cleanup()
