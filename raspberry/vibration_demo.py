#!/usr/bin/env Python
# -*- coding:utf-8 -*-
import RPi.GPIO as GPIO
import time
from senData import senddata
import sched

IO = 7

# board 编号方式，基于插座引脚
GPIO.setmode(GPIO.BOARD)

#输出模式
GPIO.setup(IO, GPIO.IN)


def my_callback(channel):
        if (GPIO.input(IO)!= '1'):
            senddata(1)
        else:
            time.sleep(300)
            if(GPIO.input(IO) == '0'):
                senddata(0)
                GPIO.remove_event_detect(IO)

while (True):
    if(GPIO.input(IO) == '1'):
        GPIO.add_event_detect(IO, GPIO.RISING, callback=my_callback)
        break
    else:
        time.sleep(2)
        continue




# while True:
#     print(GPIO.input(IO))
#     print(senddata('alpha',GPIO.input(IO)))
#     time.sleep(2)
#     print(101)


# while True:
#     start = time.time()
#     run_timer = 0
#     for i in range(1,60):
#         if(GPIO.input(IO)  == 1):
#             run_timer +=1
#         time.sleep(1)
#     end = time.time()
#     if(end - start -60 <0):
#         if run_timer >= 40:
#             senddata('alpha',1)
#         else:
#             senddata('alpha',0)


now_time = time.strftime(ISOTIMEFORMAT, time.localtime())
now_time = time.time()

TIMELIMIT = 300

while True:
    if(GPIO.input(IO) == '1'):
        while True:
            if (GPIO.input(IO) == '1'):
                now_time = time.time()
            else:
                if (time.time()-now_time>TIMELIMIT):
                    senddata()
                    now_time = time.time()
                    break
                else:
                    continue
    else:
        continue

