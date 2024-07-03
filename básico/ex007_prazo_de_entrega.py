"""Prazo de entrega determinados pela quantidade de modelos iguais"""
def obter_prazo_entrega(disco1, disco2, disco3):
    if disco1 == disco2 and disco2 == disco3:
        return 5
    if disco1 == disco2 and disco2 != disco3:
        return 15
    if disco1 != disco2 and disco2 == disco3:
        return 15
    if disco1 == disco3 and disco3 != disco2:
        return 15
    if disco1 != disco2 and disco1 != disco3 and disco2 != disco3:
        return 30

d1 = int(input())
d2 = int(input())
d3 = int(input())
prazo_entrega = obter_prazo_entrega(d1, d2, d3)
print("Disco1 =", d1)
print("Disco2 =", d2)
print("Disco3 =", d3)
print("Prazo de entrega =", prazo_entrega)