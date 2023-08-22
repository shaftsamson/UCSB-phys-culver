#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  4 12:35:58 2023

@author: samuelculver
"""
import math


a=input('Enter an intiger here: ')

while int(float(a))!=float(a) :
    a=input('Not an iniger. Enter intiger here: ')

int_a=int(float(a))

sqrt_a=math.sqrt(int_a)


factorbig_list=[]

for i in range(1,int(sqrt_a)+1):
    factor=(int_a)/i
    if factor==int(factor):
        factorbig_list.append(factor)
factorbig_list.reverse()        
        
factorsmall_list=[]        
        
for item in factorbig_list:
    factor=int_a/item
    factorsmall_list.append(factor)
factorsmall_list.reverse()

#made two four loops to reduce computation time with sqrt


factor_list=factorsmall_list+factorbig_list
#this is a list of all factors. Now each item will be checke if prime or not.

def isprime(n):
    if n <=1:
        return False
    elif n==2:
        return True
    elif n%2==0:
        return False
    else:
        for i in range(3,int(math.sqrt(n))+1,2):
            if n%i==0:
                return False
    return True            
            
primefactor_list=[]

for item in factor_list:
    if isprime(item)==True:
        primefactor_list.append(item)
        
intprimefactor_list=[int(i) for i in primefactor_list]
print(intprimefactor_list)
    


#in 12365
#out
#5, 2473
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    