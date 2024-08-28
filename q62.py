def main():

    A = ler_matriz(3, 3, "A")
    B = calcular_quadrado_matriz(A)
    
    print("\nMatriz A:")
    imprimir_matriz(A)
    print("\nMatriz B = A^2:")
    imprimir_matriz(B)

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

def calcular_quadrado_matriz(A):
    B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for i in range(3): 
        for j in range(3):
            for k in range(3):
                B[i][j] += A[i][k] * A[k][j]
    
    return B

def imprimir_matriz(matriz):

    for linha in matriz:
        print(linha)
main()
