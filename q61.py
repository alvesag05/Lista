def main():
    
    A = ler_matriz(3, 3, "A")
    B = ler_matriz(3, 3, "B")
    C = multiplicar_matrizes(A, B)
    
    print("\nMatriz A:")
    imprimir_matriz(A)
    print("\nMatriz B:")
    imprimir_matriz(B)
    print("\nMatriz C = A * B:")
    imprimir_matriz(C)

def ler_matriz(num_linhas, num_colunas, nome):
  
    matriz = []
    print(f"\nDigite os elementos da matriz {nome}:")
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            elemento = float(input(f"Digite o elemento [{i+1}][{j+1}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def multiplicar_matrizes(A, B):

    C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3):
        for j in range(3):
            for k in range(3):
                C[i][j] += A[i][k] * B[k][j]
    return C

def imprimir_matriz(matriz):
    for linha in matriz:
        print(linha)
main()
