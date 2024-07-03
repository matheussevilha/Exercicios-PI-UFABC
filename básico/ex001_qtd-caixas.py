"""Verifica a quantidade mínima de caixas necessárias para levar uma determinada carga."""

# Peso total
peso_total= int(input())

c1 = peso_total // 500
c2 = (peso_total % 500) // 100
c3 = ((peso_total % 500) % 100) // 25
c4 = (((peso_total % 500) % 100) % 25) // 1

print(c1)
print(c2)
print(c3)
print(c4)