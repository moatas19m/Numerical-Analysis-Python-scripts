from sympy import *
import pandas as pd


print("This script evaluates the root of a function using the approximation technique known as Newton's method. Note: when inputting the function, use ** to show presence of exponent, followed by the number or variable in the power. Also, input capital E for euler's number instead of just e")
print("WARNING: when inputting function, do not use quotation marks, otherwise sympify is not able to parse the input string!")
x=symbols('x')
print("for quick checking and to avoid errors, copy paste this= (E**x)+(2**(-x))+2*cos(x) - 6")
inputfunc = input("Enter the function: ")  
tolerance = float(input("Enter error tolerance, in the form 1e(Exp) where Exp is the negative exponent, for example, here it should be 1e-20:  "))
Pn=[]
Fpn=[]
iterations=[]


func = sympify(inputfunc)

print(func)

def calcfunc(a):
    return func.evalf(subs={x:a})
    

def firstderv(a):
    fdiff=diff(func, x)
    df=fdiff.doit().subs({x:a})
    d=N(df)
    return d

p0=float(input("Enter initial approximation in interval [1, 2]"))

if(firstderv(p0)==0):
    print("Error, input another initial guess")

else:
    i=1
    Pn.append(p0)
    Fpn.append(calcfunc(p0))
    iterations.append(0)
    pn=p0-(calcfunc(p0))/(firstderv(p0))
    Pn.append(pn)
    Fpn.append(calcfunc(pn))
    iterations.append(i)
    while((abs(pn-p0)/abs(pn))>=tolerance):
        p0=pn
        pn=p0-(calcfunc(p0))/(firstderv(p0))
        Pn.append(pn)
        Fpn.append(calcfunc(pn))
        i=i+1
        iterations.append(i)
    print("The approximated root is: ", pn)
    

L=[]
j=0
while(Pn[j]!=pn):
    l=(Pn[j+1]-pn)/(Pn[j]-pn)**2
    L.append(l)
    j=j+1
L.append(0)
L.append(0)
table = {'n':iterations, 'Pn':Pn,'fPn':Fpn, 'L':L} #didnt know how to take input directly from lists
df = pd.DataFrame(table)
df.set_index("n", inplace=True) #this line copied from internet
print(df)
print("Method converges to", pn, "of order 2 (quadratic convergence), with asymptotic error constant ", L[3])

df.to_csv("/home/moatasim/IBA_FALL'21/NUMERICAL ANALYSIS/Python scripts/NewtonData.txt")

import matplotlib.pyplot as plt
from numpy import *

##code below copied, I couldnt figure out the graphing tools of matplotlib

def plotNewt():
    p0 = 1.5
    p_list = [[1.5, -1.42926279833229719074], [0.78447239771941057462, -0.07671130444775364765],
              [0.73951870983205225674, -0.00072570850227082762], [0.73908517470519630166, -0.00000006943822339345]]

    x = linspace(int(p0 - 2), int(p0 + 2), 500)
    y = cos(x) - x
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.title('Newton Method')
    plt.plot(x, y, color='blue', label=f"f(x)")
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.plot(p0, p_list[0][1], 'bo', label="p0")
    plt.plot(p_list[len(p_list) - 1][0], 0, 'ro', label="p")

    for i in range(1, len(p_list)):
        x0 = p_list[i - 1][0]
        y0 = p_list[i - 1][1]
        x1 = p_list[i][0]
        y1 = 0
        x = [x0, x1]
        y = [y0, y1]
        plt.plot(x, y, color="green", linestyle='dashed', label=f"p{i - 1}")

    plt.legend()
    plt.show()
plotNewt()