# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

math = input('輸入數字: ')
eng = input('輸入數字: ')
math_new = int(math)
eng_new = int(eng)

if math_new>=90 and eng_new>=90:
    print('有獎品')
elif math_new<60 and eng_new<60:
    print('要懲罰')
elif math_new<60 or eng_new<60:
    print('要加油')
else:
    print('繼續保持')
