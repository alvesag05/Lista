def cria_matriz(dimensao):
    matriz = []
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        matriz.append(linha)
    return matriz

def imprime_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(valor, end=" ")
        print()

def main():
    dimensao = 5
    matriz = cria_matriz(dimensao)
    
    print("Matriz 5x5 com 1 na diagonal principal e 0 nos demais elementos:")
    imprime_matriz(matriz)

main()
