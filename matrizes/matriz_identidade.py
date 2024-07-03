def matriz_identidade(n:int)->list:
    M = list
    for i in range (n):
        linha = []
        for j in range (n):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        M.append(linha)
    return M