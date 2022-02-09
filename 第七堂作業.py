# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 10:08:49 2022

@author: 10407
"""

import random
noun1 = ['小狗','小貓']
verb = ['玩','丟','踢']
noun2 = ['球','玩具']

def random_smaple(list1):
    sample_word = random.sample(list1,1)[0]
    return sample_word

def random_sentence(list1,list2,list3):
    sentence = random_smaple(list1)+random_smaple(list2)+random_smaple(list3)
    return sentence

for time in range(10):
    print(random_sentence(noun1,verb,noun2))