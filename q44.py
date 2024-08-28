def busca_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j
    return -1, -1 

def imprime_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(valor, end=" ")
        print()

def main():
    
    matriz = []
    for i in range(5):
        linha = []
        for j in range(5):
            valor = float(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)
    
    print("\nMatriz 5x5:")
    imprime_matriz(matriz)
    
    valor_x = float(input("\nDigite o valor a ser buscado na matriz: "))
    
    linha_encontrada, coluna_encontrada = busca_valor(matriz, valor_x)
    
    if linha_encontrada == -1 and coluna_encontrada == -1:
        print(f"\nO valor {valor_x} não foi encontrado na matriz.")
    else:
        print(f"\nO valor {valor_x} foi encontrado na posição [{linha_encontrada+1}][{coluna_encontrada+1}] da matriz.")

main()
