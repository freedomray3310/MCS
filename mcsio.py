#!/usr/bin/python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(24,GPIO.IN,pull_up_down=GPIO.PUD_UP)

while True:
	SWitchStatus = GPIO.input(24)
	if(SwitchStatus == 0):
		print('Button pressed')
	else:
		print('Button released')

payload = {"datapoints":[{"dataChnId":"HUM","values":{"value":humidity}},{"dataChId":"Temp","values":{"value":temperature}},{"dataChnId":"Switch","values":{"value":SWitchStatus}}]}
