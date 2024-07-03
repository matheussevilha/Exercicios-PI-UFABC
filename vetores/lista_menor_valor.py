def menor_num (x: int):
    m = x[0]
    for i in range(1, len(x)):
        if m > x[i]:
            m = x[i]
    return m, x.index(m)