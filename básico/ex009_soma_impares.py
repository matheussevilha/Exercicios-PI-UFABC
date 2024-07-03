a= int(input())
b= int(input())

def somai(a,b):
    soma=0
    for i in range(a, b+1):
        if i%2 == 1:
            soma += i
    return soma

print(somai(a,b))