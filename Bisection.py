import pandas as pd

print("This program will solve only cubic equations, for higher degree polynomials, tweaking is required.")

p = float(input("Enter coefficient of x cube: "))
q = float(input("Enter coefficient of x square: "))
r = float(input("Enter coefficient of x: "))
s = float(input("Enter constant: "))
tolerance = float(input("Enter error tolerance: "))
iteration=[]
an=[]
bn=[]
Pn = []    
fpn = []
rootinit = 0.0
a = float(input("Enter lower bound of interval: "))
b = float(input("Enter upper bound of interval: "))
     
def func(p, q, r, s, x):
    return (p*(x**3) + q*(x**2) + r*x + s)
    

    
if (func(p, q, r, s, a)*func(p, q, r, s, b)>=0):
    print("error, input correct interval!")
        
else:
    i=1
    pn_1=rootinit
    pn=(a+b)/2
    Pn.append(pn)
    fpn.append(func(p,q,r,s,pn))
    iteration.append(i)
    an.append(a)
    bn.append(b)
    while ((abs(pn - pn_1)/abs(pn))>=tolerance):
        if ((func(p,q,r,s,pn))*(func(p, q, r, s, a))<0):
            b=pn
            an.append(a)
            bn.append(b)
        else:
            a=pn
            an.append(a)
            bn.append(b)
        pn_1 = pn
        pn = (a+b)/2
        i=i+1
        Pn.append(pn)
        fpn.append(func(p,q,r,s,pn))
        iteration.append(i)
        
    table = {'n':iteration, 'an':an, 'bn':bn, 'Pn':Pn,'fPn':fpn} #didnt know how to take input directly from lists
    df = pd.DataFrame(table)
    df.set_index("n", inplace=True) #copied from internet
    print(df)
         #prints the dataframe to console for easy viewing and quick checking1
df.to_csv("/home/moatasim/DATA.txt")