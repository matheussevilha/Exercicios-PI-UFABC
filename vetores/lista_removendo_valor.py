x = int(input())
frase = input()
l = []
for elemento in frase.split(' '):
    l.append(int(elemento))

def remover (x: int, l: int) -> int:
    l.remove(x)
    print(l)

remover(x,l)