# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 13:44:31 2022

@author: 10407
"""

x = 0

import random

num = random.randint(1,20)

while x < 5:
    ans = input('give me a number(1~20):')
    ans = int(ans)
    x = x+1
    
    if num == ans:
        print('yes')
        print('玩了',x,'次')
        break
    elif num < ans:
        print('smaller')
    else:
        print('bigger')

print('lose')
print('number=',num)
    


