#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 02:33:06 2021


@author: moatasim
"""

import math
import numpy as np
import matplotlib.pyplot as plt
from sympy import *


#given points to build an interpolation from:
x1 = np.linspace(-2,2,10,endpoint=False)

x=symbols('x')
inputfunc = input("Enter the function: ")  
func=sympify(inputfunc)
y1=[]

def calcfunc(a):
    return func.evalf(subs={x:a})

for val in x1:
    y1.append(calcfunc(val))
y1=np.array(y1)

#to build an interpolation for - can be one or an array of values
xvals = np.linspace(-2, 2, 100)


yexact=[]
for val in xvals:
    yexact.append(calcfunc(val))
yexact=np.array(yexact)


def v_lagrange(xval = xvals, xdat = x1, ydat = y1):
    p = 0.0
    for k in range(0, len(xdat)):
        xk = xdat[k]
        l = 1.0
        for i in range(0, len(xdat)):
            xi = xdat[i]
            if(i != k):
                l = l * ((xval - xi) / (xk - xi))
        p = p + ydat[k] * l
    return p


#returns a plot of the given estimations
yvals1 = np.array([v_lagrange(x, x1, y1) for x in xvals])
#try:
plt.plot(x1, y1, color = 'blue', label = 'Function Values')#change x1 and y1 to xvals and yexact respectively to form a smoother plot for f, and see how accurate the lagrange polynomial is
#except: pass
plt.plot(xvals, yvals1, color = 'red', label='LaGrange Values')
plt.xlabel('X Values') 
plt.ylabel('Y Values')
plt.title('Lagrange Interpolation')
plt.legend()
plt.grid()
plt.show()