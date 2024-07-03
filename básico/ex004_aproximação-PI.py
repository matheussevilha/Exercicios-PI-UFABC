"""Cálcula uma aproximação para PI."""
import math as ma

def P1 ():
    return ma.sqrt(7 + ma.sqrt(6 + ma.sqrt(5)))
print(P1())

#segunda aproximação para PI
def P2 ():
    return ma.sqrt(ma.sqrt(ma.pow(3,4)+(ma.pow(19,2)/(78 - 56))))
print(P2())