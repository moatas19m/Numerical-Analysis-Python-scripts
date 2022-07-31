#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 21:27:31 2021

@author: moatasim
"""
import numpy as np
import matplotlib.pyplot as plt
from sympy import *
from scipy.interpolate import interp1d
import pandas as pd


#given points to build an interpolation from:
xdata = np.linspace(-2,2,10,endpoint=False)

x=symbols('x')

print("for quick checking and to avoid errors, copy paste this= (E**x)+(2**(-x))+2*cos(x) - 6")
inputfunc = input("Enter the function: ")  

func=sympify(inputfunc)
ydata=np.array([], float)

def calcfunc(a):
    return func.evalf(subs={x:a})

for val in xdata:
    ydata=np.append(ydata, calcfunc(val))
    
print("Our data of x values: ", xdata)
print("Our data of y values: ", ydata)

def newton_divideddiff(xd, yd):
    #length/number of datapoints
    n = len(xd)
    #divided difference initialization
    fdd = [[None for xd in range(n)] for xd in range(n)]
    #f(X) values at different degrees
    yval = [None for xd in range(n)]
    
    #finding divided difference
    for i in range(n):
        fdd[i][0] = yd[i]
    for j in range(1,n):
        for i in range(n-j):
            fdd[i][j] = (fdd[i+1][j-1] - fdd[i][j-1])/(xd[i+j]-xd[i])
    
    #just printing dd here
    fdd_table = pd.DataFrame(fdd)
    print(fdd_table)
    fdd_table.to_csv("/home/moatasim/IBA_FALL'21/NUMERICAL ANALYSIS/Python scripts/DividedDiff.txt")

newton_divideddiff(xdata, ydata)


#to build an interpolation for - can be one or an array of values
xaxis = np.linspace(-2, 2, 100)

yexact=np.array([], float)
for val in xaxis:
    yexact=np.append(yexact, calcfunc(val))
    
#plots:
#one is xdata
#xaxis and yexact will plot the function f
#xdata and ydata will plot the generated data from function (10 values)
#xaxis and ylagr will plot the lagrange interpolation function over 100 equally spaced values

#plotting f and generated data first=>
plt.title('Our function and respective ten generated values')
plt.plot(xdata,ydata,'go', label='given data')
plt.plot(xaxis,yexact,'b-', label='exact function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best', frameon=False, fontsize=12)

plt.show()



def LagrangeInterpolation():
    ylagr=np.array([], float)  
    for xp in xaxis:
        yp=0
        for xi,yi in zip(xdata, ydata):
            yp+= yi * np.prod((xp-xdata[xdata != xi])/(xi-xdata[xdata != xi]))
        ylagr=np.append(ylagr,yp)
        
    #plotting
    plt.title('Lagrange polynomial interpolated over 100 data points')
    plt.plot(xaxis,ylagr,'r-', label='Lagrange polynomial')
    plt.xlabel('x')
    plt.ylabel('y')
    
    plt.show()
    
    return ylagr

LagrangeInterpolation()

def CubicSpline():
    #scipy's interp1d creates cubic spline interpolation function when kind='cubic' is called
    intrpfunc=interp1d(xdata, ydata, kind='cubic', bounds_error=False)
    ycspline=intrpfunc(xaxis)
    #plotting
    plt.title("Cubic spline interpolated over 10 data points")
    plt.plot(xaxis, ycspline, 'b:', label='Cubic Spline')
    #plt.plot(xaxis, yexact, 'r--', label='Exact function')
    plt.plot(xdata, ydata, 'go', label='Given data')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc='best', frameon=False, fontsize=12)
    
    plt.show()
    
    return ycspline
CubicSpline()


lag=LagrangeInterpolation()
cspline=CubicSpline()
plt.title('All 3 for comparison')
plt.plot(xdata,ydata,'ro',label='given points')
plt.plot(xaxis,lag,'b:', label='Lagrange polynomial')
plt.plot(xaxis,cspline, 'g-', label='Cubic Spline')