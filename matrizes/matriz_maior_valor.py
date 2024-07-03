def maior_valor (M:list) -> int:
    maior = M[0][0]

    for i in range(len(M)):
        for j in range(len(M[0])):
            if maior < M[i][j]:
                maior = M[i][j]
    return maior