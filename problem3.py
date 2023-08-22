#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 16:42:47 2023

@author: samuelculver
"""
#part a
a=input('Write a string with at least 3 words: ')
b=a.split()
l=len(b)

#part b
while l < 3:
    a=input('Less than three words detected. Please write a string with at least 3 words you illiterate.: ')
    b=a.split()
    l=len(b)
  
print("Words in string")

#part c    
for item in b:
     print(item)
print("")

print("First three characters")

#Part d
print(a[:3])
print("")

print("Last three characters")

#part e
print(a[-3:])
print("")

print("First half of the string, including middle character")

#part f
l_a=(int(round(len(a))/2))

print(a[:l_a])
print("")

print("Last half of the string, including middle character")

#part g

print(a[l_a:])
print("")

print("words in reverse order")

#part h
b.reverse()
print(" ".join(b))

b.reverse()

print("")
print("Words in the string alphabetized ")

#part i
sorted_list=sorted(b)
print(" ".join(sorted_list))

print("")
print("Each character of the string")

#part j
for i in range(len(a)):
    print(a[i])
    
print("")
print("Hexadecimal values")

#part k

for i in range(len(a)):
    print(ord(a[i]))

    

