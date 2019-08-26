# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:24:30 2019

@author: chinmay
"""
test=[111,1111,112,12,13,1,445,1000,2112,1221,90,80,5,7,8,9,190,200,212,567,777,899,123,22,45,77,8,9,10,233,221,34,222,190,80,70,35,32,12,0]
i=0
j=len(test)-1
nat_sum=0
oppo_sum=0

while i<j:
    if test[i]>test[j]:
        nat_sum+=test[i]
        oppo_sum+=test[j]
    else:
        nat_sum+=test[j]
        oppo_sum+=test[i]
    i+=1
    j-=1
print(nat_sum,oppo_sum)
    
    
    
            