#THIS PROGRAM SOLVES QUADRATIC EQATIONS ax^2+bx+c

import math as m
a=float(input("a:"))
b=float(input("b:"))
c=float(input("c:"))

det=float((b**2)-(4*a*c))
if det >= 0:
    x1=(-b + m.sqrt(det)/2*a)
    x2=(-b - m.sqrt(det)/2*a)
    print("X1:",x1, "\nx2:",x2)
else:
    Re=float(-b/(2*a))
    Im=float(m.sqrt(-det))/(2*a)
    print("X1:",Re,"+",Im,"i")
    print("X1:",Re,"-",Im,"i")