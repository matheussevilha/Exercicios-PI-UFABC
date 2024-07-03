def matriz_bordas (m: int,n: int) -> list:
    M = []
    for i in range(m):
        linha = []
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                linha.append(1)
            else:
                linha.append(0)
        M.append(linha)
    return M