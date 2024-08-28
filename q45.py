def cria_terceira_matriz(matriz1, matriz2):
    terceira_matriz = []
    for i in range(len(matriz1)):
        linha = []
        for j in range(len(matriz1[i])):
            if matriz1[i][j] > matriz2[i][j]:
                linha.append(matriz1[i][j])
            else:
                linha.append(matriz2[i][j])
        terceira_matriz.append(linha)
    return terceira_matriz

def imprime_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(valor, end=" ")
        print()

def main():
    
    matriz1 = []
    matriz2 = []
    
    print("Preencha a primeira matriz 4x4:")
    for i in range(4):
        linha1 = []
        for j in range(4):
            valor = float(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))
            linha1.append(valor)
        matriz1.append(linha1)
    
    print("\nPreencha a segunda matriz 4x4:")
    for i in range(4):
        linha2 = []
        for j in range(4):
            valor = float(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))
            linha2.append(valor)
        matriz2.append(linha2)
    
    matriz3 = cria_terceira_matriz(matriz1, matriz2)
   
    print("\nMatriz 1:")
    imprime_matriz(matriz1)
    
    print("\nMatriz 2:")
    imprime_matriz(matriz2)
    
    print("\nTerceira matriz com os maiores valores de cada posição:")
    imprime_matriz(matriz3)

main()
