import time
import sched
from senData import senddata
import RPi.GPIO as GPIO
# ISOTIMEFORMAT='%Y-%m-%d %X'
# now_time = time.strftime(ISOTIMEFORMAT, time.localtime())
#
# print(time.time())
#
# a = time.time()
# print(a)
#
# time.sleep(1)
#
# b = time.time()
#
# print(b)
#
# if(b-a >1):
#     print('YES')
# else:
#     print('Halloworld')

schedule = sched.scheduler(time.time, time.sleep)

def func(string1, float1):
    if (GPIO.input(IO) == '0'):
        senddata()


now_time = time.strftime(ISOTIMEFORMAT, time.localtime())
now_time = time.time()

TIMELIMIT = 10

while True:
    if(GPIO.input(IO) == '0'):
        schedule.enter(5, 0, func, ("test1", time.time()))
    else:
        continue