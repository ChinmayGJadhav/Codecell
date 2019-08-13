# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 19:24:30 2019

@author: chinmay
"""
test=[10, 256,511,4097,8194]
prices=[1,2,4,8,16,32,64,128,256,512,1024,2048]
prices.reverse()
ans=1
count=0
for i in test:
    for j in range(len(prices)):
        if prices[j]<=i:
            break
    p=prices[j:len(prices)]
    '''temp=i-p[0]
    count+=1
    print(temp)
    if temp==0:
        print(count)
        continue'''
    temp=i
    s=0
    while True:
        if p[s]<=temp:
            count+=1
            temp-=p[s]
        else:
            s+=1
        if temp==0:
            break
    ans=ans*count
    count=0    
print(ans)
            
        
    
    
    
            