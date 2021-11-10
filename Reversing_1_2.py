# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 21:42:40 2021

@author: lenovo
"""

def reverse(word):
    a = ""
    for i in range(1, len(word) + 1):
        a += word[len(word) - i]
    return a

print(reverse("Edyoda")) 