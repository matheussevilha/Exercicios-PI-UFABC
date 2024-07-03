def seg_menor (x: int):
    x.sort()
    i = 0
    while x[i] == x[0]:
        i = i + 1
    return x[i]

x= [3,3,5,6,77,7,8,3,5,4,6,9]
print(seg_menor(x))