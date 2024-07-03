""" Comparando datas:

 (1) - primeira data é mais recente
 (0) - as datas são iguais
(-1) - a segunda data é mais recente"""

def comparar_datas(d1, m1, a1, d2, m2, a2):
    if a1 == a2:
        if m1 == m2:
            if d1 == d2:
                return 0
            else:
                if d1 > d2:
                    return 1
                else:
                    return -1
        else:
            if m1 > m2:
                return 1
            else:
                return -1
    else:
        if a1>a2:
            return 1
        else:
            return -1