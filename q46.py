def gera_matriz():
    matriz = []
    for i in range(10):
        linha = []
        for j in range(10):
            if i < j:
                elemento = 2*i + 7*j
            elif i == j:
                elemento = 3*i**2 + 1
            else:
                elemento = 4*i**3 + 5*j**2 + 1
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def imprime_matriz(matriz):
    for linha in matriz:
        for valor in linha:
            print(f"{valor:4}", end=" ")
        print()

def main():
    matriz = gera_matriz()
    
    print("Matriz 10x10 gerada:")
    imprime_matriz(matriz)

main()
