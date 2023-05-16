# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:22:42 2023

@author: Alunc
"""

import math


print(math.sqrt(9))

print(math.sin(45))

print(math.cos(52))

print(math.log(80))

print(math.log(100, 10))

print(math.e)

print(math.pi)



#datatime

import datetime

print(datetime.date.today())

print(datetime.datetime.now())

data = datetime.date(2020,7,10)

print(data.day,data.month,data.year)

horario = datetime.datetime(2020,7,10, 7, 30, 0)

print(horario)

print(horario.hour,horario.minute,horario.second)



#random
import random

print(random.randint(1,5))

print(random.randrange(0,10,3))

x= ['k','d',12,'34-l','x']

print(random.choice(x))



#time
import time as tm

print(tm.time())
print('sleep', tm.sleep(3))

































