#!/usr/bin/env Python
# -*- coding:utf-8 -*-

import requests
import time

def senddata(mid,value):
    ISOTIMEFORMAT='%Y-%m-%d %X'

    host = "192.168.1.106"

    # a =time.time()
    # time.sleep(1)
    # b = time.time()
    # print(b-a)
    print(time.time())
    time_stamp = time.time()

    read_time = time.strftime(ISOTIMEFORMAT, time.localtime())
    #print(time.strftime(ISOTIMEFORMAT, time.localtime()))

    data_dict = {'mid': mid ,'value':value ,'timestamp':time_stamp ,'read_time':read_time}
    url = host + "/data_demo.php"
    r = requests.post(url, data=data_dict)
    if (r.status_code == 200):
        #print("success")
        return 0
    else:
        return -1

