# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 11:53:00 2022

@author: 10407
"""

import random

num = random.randint(1,10)

while True:
    ans = input('give me a number(1~10):')
    ans = int(ans)
    if num == ans:
        print('yes')
        break
print('hello')