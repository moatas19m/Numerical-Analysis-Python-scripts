#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 17:06:00 2021

@author: moatasim
"""

from sympy import *
import pandas as pd

print("This script evaluates the root of a function using the approximation technique known as the Fixed-Point method. Note: when inputting the function, use ** to show presence of exponent, followed by the number or variable in the power. Also, input capital E for euler's number instead of just e")
print("WARNING: when inputting function, do not use quotation marks, otherwise sympify is not able to parse the input string!")
x=symbols('x')
print("for quick checking and to avoid errors, copy paste this= (E**x)+(2**(-x))+2*cos(x) - 6+x")
inputfunc = input("Enter the function: ")  
tolerance = float(input("Enter error tolerance, in the form 1e(Exp) where Exp is the negative exponent, for example, here it should be 1e-20:  "))
Pn=[]
iterations=[]


func = sympify(inputfunc)

print(func)


def calcfunc(a):
    return func.evalf(subs={x:a})
    
i=0
p0=float(input("Enter initial approximation in interval [1, 2]"))
iterations.append(i)
Pn.append(p0)
pn=calcfunc(p0)
i=i+1
iterations.append(i)
Pn.append(pn)
while((abs(pn-p0)/abs(pn))>=tolerance):
    p0=pn
    pn=calcfunc(p0)
    i=i+1
    iterations.append(i)
    Pn.append(pn)
print("the approximated root is: ",pn)
L=[]
j=0
while(Pn[j]!=pn):
    l=(Pn[j+1]-pn)/(Pn[j]-pn)**2
    L.append(l)
    j=j+1
L.append(0)
L.append(0)
table = {'n':iterations, 'Pn':Pn, 'L':L} #didnt know how to take input directly from lists
df = pd.DataFrame(table)
df.set_index("n", inplace=True) #this line copied from internet
print(df)
print("Method converges to", pn, "of order 2 (quadratic convergence), with asymptotic error constant ", L[3])

df.to_csv("/home/moatasim/IBA_FALL'21/NUMERICAL ANALYSIS/Python scripts/FixedPoint.txt")
    