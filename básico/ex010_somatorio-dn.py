"""somatório com n diminuido no denominador e crescendo no numerador."""
n = int(input())
def somared(n):
    soma = 0
    for i in range (n,0,-1):
        soma += (n - (i-1)) / i