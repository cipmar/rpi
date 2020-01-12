import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
#set the trigger pin as OUTPUT and the echo as INPUT
trigPin = 16
echoPin = 18

GPIO.setup(trigPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)

GPIO.output(trigPin, GPIO.HIGH)

#sleep 0.00001 s and set the trigger to LOW
time.sleep(0.00001)
GPIO.output(trigPin, GPIO.LOW)

#save the start and stop times
start = time.time()
stop = time.time()

#modify the start time to be the last time until the echo becomes HIGH
while GPIO.input(echoPin) == 0:
    start = time.time()

#modify the stop time to be the last time until the echo becomes LOW
while GPIO.input(echoPin) == 1:
    stop = time.time()

#get the duration of the echo pin as HIGH
duration = stop - start
#calculate the distance
soundSpeed = 34300 # cm/s
distance = soundSpeed * duration / 2

#the reading can be erroneous, and we will print
#the distance only if it is lower than the specified value
if distance < 3400:
    #display the distance in console
    print ("Distance = %.2f" % distance)

:GPIO.cleanup()
