# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:51:30 2019

@author: chinmay
"""


c=3
L=list()
ans=0
final_ans=0
while c!=0: 
    T=int(input())
    L=input().split(" ")
    for i in range(T):
        L[i]=int(L[i])
    for i in range(T):
        for j in range(i+1,T):
            ans+= L[i]&L[j]
    c-=1 
    final_ans+=ans%101
    ans=0
print(final_ans)     
