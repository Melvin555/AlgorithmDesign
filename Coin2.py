# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 16:33:19 2017

@author: Melvin
"""
x = {'a':50,'b':50,'c':50,'d':50,'e':50,'f':50,'g':50,'h':50,'i':50,'j':50,'k':70,'l':50,}
array = []
for i in range(12):
    m = input("Please insert charachter: ")
    array.append(str(m))



def searchCoin(leftorright):
    i = 0
    j = 0
    leftorright_weight = []
    for i in range(4):
        leftorright_weight[i].append(x[leftorright[i]])
    for j in range(4):
        if leftorright_weight[j]<leftorright_weight[j+1]:
            fakeCoin = leftorright[j]
            status = 'Light'
            return fakeCoin, status
        elif leftorright_weight[j]>leftorright_weight[j+1]:
            fakeCoin = leftorright[j]
            status = 'Heavy'
            return fakeCoin, status
        else:
            status = 'Fair'
            return status

lefthand = array[:4]
righthand = array[4:8]
keep = array[8:]

lefthand_weight = x[lefthand[0]]+x[lefthand[1]]+x[lefthand[2]]+x[lefthand[3]]
righthand_weight = x[righthand[0]]+x[righthand[1]]+x[righthand[2]]+x[righthand[3]]
currentScale = lefthand + righthand
print("current scale consist of",lefthand," and ",righthand)
print("in keep there are ", keep)

if lefthand_weight==righthand_weight:
    lefthand[1] = keep[0]
    lefthand[2] = keep[1]
    righthand[1] = keep[2]
    righthand[2] = keep[3]
    [fakeCoin, status] = searchCoin(lefthand)
    if status == 'Fair':
        [fakeCoin, status] = searchCoin(righthand)

else:
    [fakeCoin, status] = searchCoin(lefthand)
    if status == 'Fair':
        [fakeCoin, status] = searchCoin(righthand)

print(fakeCoin)
print(status)
    



#array = ['abcd', 'efgh']
#for i in range(2):
#    if 'b' in array[i]:
#        print(array[i])