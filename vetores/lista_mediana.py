def mediana (x: int):
    if len(x)%2 == 0:
        soma = 0
        for i in (int(len(x)/2) - 1),int(len(x)/2):
            soma = soma + x[i]/2
        return soma
    else:
        i = ((len(x) + 1)/2) - 1
        return x[i]

x = [1, 2, 3, 4, 5, 6]
print(mediana(x))