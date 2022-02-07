# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 11:31:13 2022

@author: 10407
"""

scores = [['chris',83],
          ['david',96],
          ['bill',92],
          ['amy',59],
          ['james',77]
          ['happy',88]
          ['daniel',46]
          ['olivier',64]
          ['sunstein',76]
          ['apple',84]]

print(scores[1][0])

student_name = [scores[i][0] for i in range(len(scores))]
print(student_name)

student_score = [scores[i][1] for i in range(len(scores))]
print(student_score)

max_index = student_score.index(max(student_score))
print(f'higgest:{student_name[max_index]},{max(student_score)}')

min_index = student_score.index(max(student_score))
print(f'lowest:{student_name[min_index]},{min(student_score)}')