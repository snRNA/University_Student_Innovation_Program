#!/usr/bin/env Python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
from senData import senddata

IO = 7

# board 编号方式，基于插座引脚
GPIO.setmode(GPIO.BOARD)

#输出模式
GPIO.setup(IO, GPIO.IN)


# while True:
#     print(GPIO.input(IO))
#     print(senddata('alpha',GPIO.input(IO)))
#     time.sleep(2)
#     print(101)


while True:
    start = time.time()
    run_timer = 0
    for i in range(1,60):
        if(GPIO.input(IO)  == 1):
            run_timer +=1
        time.sleep(1)
    end = time.time()
    if(end - start -60 <0):
        if run_timer >= 40:
            senddata('alpha',1)
        else:
            senddata('alpha',0)
