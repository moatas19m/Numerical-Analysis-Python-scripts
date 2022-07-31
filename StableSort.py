#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 15:27:14 2022

@author: moatasim
"""

import numpy as np

len1 = int(input("Enter size of list 1, b/w 8 and 64k: "))
len2 = int(input("Enter size of list 2, b/w 8 and 64k: "))

list1 = np.linspace(0,1,len1,endpoint=False)
list2 = np.linspace(0,1,len2,endpoint=False)

list1=np.delete(list1,0)
list2=np.delete(list2,0)

list1.sort()
list2.sort()

print(list1, "\n")
print(list2, "\n")

tlist=[]

def buildTuple():
    for i in range(0,len1-1):
        tlist.append((i, list1[i]))
    for i in range(0,len2-1):
        tlist.append(((i+len1-1), list2[i]))
    print(tlist,"\n")
    
buildTuple()

def take_second(elem):
    return elem[1]

finalSorted=sorted(tlist, key=take_second)
print("Final stable sorted list is: \n", finalSorted)