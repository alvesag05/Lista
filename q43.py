def encontra_maior_valor(matriz):
    maior_valor = matriz[0][0]
    linha_maior = 0
    coluna_maior = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > maior_valor:
                maior_valor = matriz[i][j]
                linha_maior = i
                coluna_maior = j
    
    return linha_maior, coluna_maior

def imprime_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(valor, end=" ")
        print()

def main():

    matriz = []
    for i in range(4):
        linha = []
        for j in range(4):
            valor = float(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)
    
    print("\nMatriz 4x4:")
    imprime_matriz(matriz)
    
    linha_maior, coluna_maior = encontra_maior_valor(matriz)
    
    print(f"\nO maior valor encontrado na matriz é {matriz[linha_maior][coluna_maior]}, na posição [{linha_maior+1}][{coluna_maior+1}].")

main()
