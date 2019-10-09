# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 15:44:44 2017

@author: Melvin
"""
def isLight(curChar):
    for i in range(3):
        







n = input("Please insert the number of set: ")
i = 0
while n > 0:
    for i in range(3):
        array = []
        m = input("The name of coins are: ")
        array.append(str(m))
    for curChar in range('L'):
        if isLight(curChar):
            print(curChar,"light")
            break
        if isHeavy(curChar):
            print(curChar,"Heavy")
            break
    n = n - 1

