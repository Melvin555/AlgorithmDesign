# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 10:31:51 2017

@author: Melvin
"""
def MergeSort(array):
    if len(array)>1:
        mid = len(array)//2
        lefthalf = array[:mid]
        righthalf = array[mid:]
        
        MergeSort(lefthalf)
        MergeSort(righthalf)
        
        i = 0
        j = 0
        k = 0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                array[k] = lefthalf[i]
                i = i + 1
            else:
                array[k] = righthalf[j]
                j = j + 1
            k = k + 1
        while i<len(lefthalf):
            array[k] = lefthalf[i]
            i = i + 1
            k = k + 1
        while j<len(righthalf):
            array[k] = righthalf[j]
            j = j + 1
            k = k + 1


array = []
n = input("Please input the number of values: ")
for l in range(int(n)):
    m = input("The value is: ")
    array.append(int(m))

MergeSort(array)
print("\nThe value after sorting is: \n")
print(array)