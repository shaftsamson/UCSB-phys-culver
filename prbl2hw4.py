#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  2 21:26:23 2023

@author: samuelculver
"""

import pandas as pd

f = pd.read_csv('/Users/samuelculver/Desktop/problem2.csv')

rows = len(f)

people = []

for i in range(rows):
    person = {'last': f['column1'][i], 'first': f['column2'][i], 'color': f['column3'][i],
              'food': f['column4'][i], 'field': f['column5'][i], 'physicist': f['column6'][i]}
    people.append(person)


b = '1'
while b == '1':
    print('Here are the available keys: color, food, field, physicist')
    a = input('Please enter a key of your choice here: ')
    alpha_people = sorted(people, key=lambda x: x['last'])

    for i in range(rows):
        print(alpha_people[i]['last'], alpha_people[i]
              ['first'], ':', alpha_people[i][a])

    b = input('If you would like to repeat the process with the same or different key, enter 1. Else, enter any other value: ')


#input color
#out
#Bird Flyer: Sky Blue
#Gator Croc: Green
#Jerry Pogors: Blue

#input food
#out
#Bird Flyer : Insects
#Gator Croc : Large Mammals
#Jerry Pogors : Pizza

#input field
#out
#Bird Flyer : Aerodynamics
#Gator Croc : Fluid Mechanics
#Jerry Pogors : Mechanics

#input physicist
#out
#Bird Flyer : The Wright Brothers
#Gator Croc : Bernuli
#Jerry Pogors : Einstein








