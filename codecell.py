# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 16:19:50 2019

@author: chinmay
"""

elemt=input()
D=elemt.split("/")
date=int(D[0])
month=int(D[1])
year=int(D[2])

k=(year%7)-1
A=dict()
month_day=dict()
for i in range(1,13):
    month_day.update({i:k%7})
    k+=3
print(month_day)
start=month_day[month]
for i in range(1,7):
    A.update({i:start%7})
    start+=1
A.update({0:start%7})
print(A)
print(A[date%7])



    
    