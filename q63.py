def proxima_jogada(tabuleiro):

    for i in range(3):
  
        if tabuleiro[i][0] == -1 and tabuleiro[i][1] == -1 and tabuleiro[i][2] == 0:
            return (i, 2)
        elif tabuleiro[i][0] == -1 and tabuleiro[i][2] == -1 and tabuleiro[i][1] == 0:
            return (i, 1)
        elif tabuleiro[i][1] == -1 and tabuleiro[i][2] == -1 and tabuleiro[i][0] == 0:
            return (i, 0)
        
        if tabuleiro[0][i] == -1 and tabuleiro[1][i] == -1 and tabuleiro[2][i] == 0:
            return (2, i)
        elif tabuleiro[0][i] == -1 and tabuleiro[2][i] == -1 and tabuleiro[1][i] == 0:
            return (1, i)
        elif tabuleiro[1][i] == -1 and tabuleiro[2][i] == -1 and tabuleiro[0][i] == 0:
            return (0, i)
    
    if tabuleiro[0][0] == -1 and tabuleiro[1][1] == -1 and tabuleiro[2][2] == 0:
        return (2, 2)
    elif tabuleiro[0][0] == -1 and tabuleiro[2][2] == -1 and tabuleiro[1][1] == 0:
        return (1, 1)
    elif tabuleiro[1][1] == -1 and tabuleiro[2][2] == -1 and tabuleiro[0][0] == 0:
        return (0, 0)
    
    if tabuleiro[0][2] == -1 and tabuleiro[1][1] == -1 and tabuleiro[2][0] == 0:
        return (2, 0)
    elif tabuleiro[0][2] == -1 and tabuleiro[2][0] == -1 and tabuleiro[1][1] == 0:
        return (1, 1)
    elif tabuleiro[1][1] == -1 and tabuleiro[2][0] == -1 and tabuleiro[0][2] == 0:
        return (0, 2)
    
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 0:
                return (i, j)
    
    return None 

tabuleiro = [
    [-1, 1, 1],
    [-1, -1, 0],
    [0, 1, 0]
]

print("Tabuleiro atual:")
for linha in tabuleiro:
    print(linha)

print("\nPróxima jogada:")
jogada = proxima_jogada(tabuleiro)
if jogada:
    print(f"Jogar na posição {jogada}")
else:
    print("Não há mais jogadas possíveis.")
