"""Criando uma lista a partir de valores fornecidos pelo usuário."""

f = input('escreva os valores com um espaço entre eles:')
l = list()
for elemento in f.split(' '):
    l.append(int(elemento))
print(l)