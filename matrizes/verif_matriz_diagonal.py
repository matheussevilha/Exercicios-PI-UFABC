def diagonal (M:list) -> bool:
    n_linhas = len(M)
    n_colunas = len(M[0])
    if n_linhas != n_colunas:
        return False

    for i in range (n_linhas):
        for j in range (n_colunas):
            if i != j and M[i][j] != 0:
                return False
    return True