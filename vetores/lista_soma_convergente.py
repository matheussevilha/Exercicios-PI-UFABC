def soma_c (l : int) -> bool:
    a = 0
    z = len(l) - 1
    t = 1
    while a < (len(l)/2) - 1:
        if l[a] + l[z] > l[a+1] + l[z-1]:
            t = 1
        else:
            t = t + 1
            break
        a = a + 1
        z = z - 1
    if t == 1:
        return True
    if t!= 1:
        return False

x = []
n = int(input())
for i in range (0,n):
    num = int(input())
    x.append(num)

print('É uma soma convergente?',soma_c(x))

# ----------- resolução slide ---------------------

def sc(v:int):
    g = len(v)
    soma_ponta = v[0] + v[g-1]
    i = 1
    j = g-2
    while i < j:
        if soma_ponta > v[i] + v[j]:
            soma_ponta = v[i] + v[j]
            i = i + 1
            j = j -1
        else:
            break
    if i > j:
        print('sim')
    else:
        print('não')

hj = []
r = int(input())
for i in range (0,r):
    num = int(input())
    hj.append(num)

sc(hj)