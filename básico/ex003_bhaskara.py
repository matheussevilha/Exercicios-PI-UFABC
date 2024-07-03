"""Cálculo de função quadrática a partir dos coeficientes."""

import math

a= int(input())
b= int(input())
c= int(input())

delta= b**2-4*a*c

if delta < 0:
    print('Sem solucao real!')
elif delta == 0:
    x1= (-b + math.sqrt(delta))/2*a
    print('{:.2f}.format(x1)')
else:
    x1= (-b + math.sqrt(delta))/2*a
    x2= (-b - math.sqrt(delta))/2*a
    if x1>x2:
        print('x1 ={:.2f}'.format(x1))
        print('x2 ={:.2f}'.format(x2))
    if x2>x1:
        print('x1 ={:.2f}.format(x2)')
        print('x2 ={:.2f}.format(x1)')