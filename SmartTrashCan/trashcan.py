#CONFIG

clientID = "<INSERT A TRASHCAN ID>"
adafruitID = "<ENTER YOUR ADAFRUIT ID>"
adafruitKey = "<ENTER YOUR ADAFRUIT KEY>"
broker_address = "io.adafruit.com" 
pubTopic = "<ADAFRUIT ID>/feeds/<TRASHCAN ID>"

#------------------------------------------------


import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt 

client = mqtt.Client(clientID) 
client.username_pw_set(adafruitID, adafruitKey)
client.connect(broker_address) 

GPIO.setmode(GPIO.BCM)

TRIG = 5 
ECHO = 6

print "Measuring Distance"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

GPIO.output(TRIG, False)
print "Waiting For Sensor"

while 1:
    time.sleep(2)

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:
        pulse_start = time.time()

    while GPIO.input(ECHO)==1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration * 17150

    distance = round(distance, 2)

    client.publish(pubTopic,distance)
    print "Distance:",distance,"cm"

GPIO.cleanup()
