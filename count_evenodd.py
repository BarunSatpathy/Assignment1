# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 21:50:51 2021

@author: lenovo
"""

sample = {1, 2, 3, 4, 5, 6, 7, 8, 9}
print("Even and Odd Set Items = ", sample)

evenCount = oddCount = 0

for n in sample:
    if(n % 2 == 0):
        evenCount = evenCount + 1
    else:
        oddCount = oddCount + 1

print("The Count of Even Numbers in Sample = ", evenCount)
print("The Count of Odd  Numbers in Sample = ", oddCount)
