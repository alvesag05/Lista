import random

def gerar_matriz():
    matriz = []
    tamanho = 4 
    
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            valor = random.randint(1, 20) 
            linha.append(valor)
        matriz.append(linha)
    
    return matriz

def matriz_triangular_inferior(matriz):
    tamanho = len(matriz)
    
    for i in range(tamanho):
        for j in range(i + 1, tamanho):
            matriz[i][j] = 0  
    
    return matriz

def main():
   
    matriz_original = gerar_matriz()
    
    matriz_transformada = [linha[:] for linha in matriz_original]
    
    matriz_transformada = matriz_triangular_inferior(matriz_transformada)
    
    print("Matriz Original 4x4:")
    for linha in matriz_original:
        print(linha)
    
    print("\nMatriz Transformada em Triangular Inferior 4x4:")
    for linha in matriz_transformada:
        print(linha)

main()
