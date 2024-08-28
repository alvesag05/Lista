def cria_matriz(dimensao):
    matriz = []
    for i in range(dimensao):
        linha = []
        for j in range(dimensao):
            linha.append(i * j)
        matriz.append(linha)
    return matriz

def imprime_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(valor, end=" ")
        print()

def main():
    dimensao = 5  # Dimensão da matriz (5x5 no exemplo)
    matriz = cria_matriz(dimensao)
    
    print(f"Matriz {dimensao}x{dimensao} com o produto dos índices da linha e coluna:")
    imprime_matriz(matriz)

main()
