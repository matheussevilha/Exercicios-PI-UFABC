"""Realiza a verificaçã de naves a partir de seu número de série."""

import math as mt

ns = int(input())

def sep1(ns):
    c1 = (ns // mt.pow(10, 5)) * mt.pow(10, 5)
    ns = ns - c1
    c2 = (ns // mt.pow(10, 4)) * mt.pow(10, 4)
    ns = ns - c2
    soma1 = (c1 + c2) / 10 ** 4
    c3 = (ns // mt.pow(10, 3)) * mt.pow(10, 3)
    ns = ns - c3
    c4 = (ns // mt.pow(10, 2)) * mt.pow(10, 2)
    ns = ns - c4
    soma2 = (c3 + c4) / 100
    c5 = (ns // mt.pow(10, 1)) * 10
    ns = ns - c5
    c6 = ns * 1
    soma3 = c5 + c6
    return soma1, soma2, soma3

soma1, soma2, soma3 = sep1(ns)

if soma1 == 80:
    print('Marte')
elif soma1 == 81:
    print('Saturno')
elif soma1 == 90:
    print('Netuno')
else:
    print('HD21749b')

if soma2 == 60:
    print('A6000')
elif soma2 == 61:
    print('B7500')
elif soma2 == 62:
    print('C9000')

if soma3 == 80:
    print('Marte')
elif soma3 == 81:
    print('Saturno')
elif soma3 == 90:
    print('Netuno')
else:
    print('HD21749b')