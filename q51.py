def matriz_transposta(matriz):
    tamanho = len(matriz)
    transposta = [[0]*tamanho for _ in range(tamanho)]
    
    for i in range(tamanho):
        for j in range(tamanho):
            transposta[j][i] = matriz[i][j]
    
    return transposta

def main():
   
    matriz = []
    tamanho = 3 
    
    print("Digite os elementos da matriz 3x3:")
    for i in range(tamanho):
        linha = []
        for j in range(tamanho):
            valor = float(input(f"Digite o elemento [{i+1}][{j+1}]: "))
            linha.append(valor)
        matriz.append(linha)
    
    transposta = matriz_transposta(matriz)
    
    print("\nMatriz original 3x3:")
    for linha in matriz:
        print(linha)
    
    print("\nMatriz transposta 3x3:")
    for linha in transposta:
        print(linha)

main()
