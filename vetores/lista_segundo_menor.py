def segmenor_num (x: int):
    m = x[0]
    for i in range(1, len(x)):
        if m > x[i]:
            m = x[i]
    x.remove(m)
    m = x[0]
    for i in range(1, len(x)):
        if m > x[i]:
            m = x[i]
    return m, x.index(m)+1


list = [33, 44, 55, 66, 77, 99, 74]
print(segmenor_num(list))