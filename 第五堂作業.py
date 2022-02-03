# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 21:24:07 2022

@author: 10407
"""

scores = []

for i in range(3):
    socre = int(input('input score:'))
    scores.append(scores)
    
print(scores)

total = 0

highest = 0
lowest = 100

for i in scores:
    if i > highest:
        highest = i
    if i < lowest:
        lowest = i
    total = total + i

print('total:',total)
print('highest:',highest)
print('lowest:',lowest)
print('mean:',total/3)