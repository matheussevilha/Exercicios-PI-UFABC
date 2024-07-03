def aprox_pi ():
    soma=1
    t =1
    for i in range (3, 1999,2):
        soma += 1/(i*((-1)**t))
        t +=1
    return 4*soma
print(aprox_pi())