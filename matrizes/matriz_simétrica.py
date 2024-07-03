def matriz_bordas (m: int,n: int) -> list:
    M = []
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(abs(i-j))
        M.append(linha)
    return M