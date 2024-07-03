def semiparticionado (x:int):
    ii = 0
    ifi = len(x) - 1
    while ii != len(x)//2:
        a = x[ii]
        z = x[ifi]
        if a > z:
            x[ii] = z
            x[ifi] = a
        ii += 1
        ifi += (-1)
        if ii == ifi:
            break
    return x

x = [6,5,4,3,2,1]

print(semiparticionado(x))