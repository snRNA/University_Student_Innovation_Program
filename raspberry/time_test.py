# -*- coding:utf-8 -*-
import time

start = time.time()
a = 0
for i in range(1,10):
    a+=1
    time.sleep(2)

end = time.time()

print(end-start-60)
