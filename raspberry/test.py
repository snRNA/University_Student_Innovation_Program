#!/usr/bin/env Python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time

IO=7

GPIO.setmode(GPIO.BOARD)

GPIO.setup(IO, GPIO.IN)

while True:
	print (GPIO.input(IO))
	time.sleep(2)
	print(101)
