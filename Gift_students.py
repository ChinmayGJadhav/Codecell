# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 19:23:44 2019

@author: chinmay
"""

test=[]
rating=[]

test=list(map(int,input().split(",")))
for i in range(len(test)):
    rating.append(-1)
print(rating)
ans=test.index(min(test))
i1=ans-1
i2=ans+1
rating[ans]=1
for i in range(i1,-1,-1):
    if test[i]==test[i+1]:
        rating[i]=rating[i+1]
    elif test[i]<test[i+1]:
        rating[i]=rating[i+1]-1
    else :
        rating[i]=rating[i+1]+1

for i in range(i2,len(test)):
    if test[i]==test[i-1]:
        rating[i]=rating[i-1]
    elif test[i]<test[i-1]:
        rating[i]=rating[i-1]-1
    else:
        rating[i]=rating[i-1]+1
       
print(rating)
print(sum(rating))    
