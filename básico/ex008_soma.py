a= int(input())
b= int(input())
def soma (a,b):
    s=0
    for i in (a,b):
        s += i
    return s

print(soma(a,b))