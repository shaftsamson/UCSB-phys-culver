#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 16:36:55 2023

@author: samuelculver
"""

import requests

datastring=requests.get('http://web.physics.ucsb.edu/~phys129/lipman/').text

update_indexf=datastring.find('Latest update: <span class="greenss">')

update_indexb=datastring.find('</span></p>')



date=(datastring[(update_indexf)+37:(update_indexb)])
date_nonpsb=date.replace('&nbsp;',' ')

print(date_nonpsb)

#This does essentially the same thing as problem 2 but we dont have to deal with a raw 
#socket and we get to use requests instead to ge the data from the site, 
#which is much more straightforward