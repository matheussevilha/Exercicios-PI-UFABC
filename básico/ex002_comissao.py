"""Exercício para verificar se a meta de vendas foi atingida e qual comissão será recebida."""

sav= float(input())
tv= float(input())
comissao = 0.2*tv
print('{:.2f}'.format(comissao))
if tv >= 2.5*sav:
    print('Atingiu meta de vendas')
else:
    print('Nao atingiu meta de vendas')