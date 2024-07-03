def matriz_uns(m:int,n:int) ->list:
    M = []
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(1)
        M.append(linha)
    return M