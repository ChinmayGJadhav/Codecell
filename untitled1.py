# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:51:30 2019

@author: chinmay
"""

x,y,z=input().split(" ")
x=int(x)
y=int(y)
z=int(z)
if x<y:
    ans=x-z
else:
    for i in range(1,z+1):
        if x>y:
            x-=2
        else:
            x-=1
    ans=x
print(ans)