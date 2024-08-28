def soma_abaixo_diagonal_principal(matriz):
    soma = 0
    tamanho = len(matriz)
    
    for i in range(tamanho):
        for j in range(tamanho):
            if j < i:  
                soma += matriz[i][j]
    
    return soma

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
    
    resultado = soma_abaixo_diagonal_principal(matriz)
    
    print("\nMatriz 3x3:")
    for linha in matriz:
        print(linha)
    
    print(f"\nA soma dos elementos abaixo da diagonal principal é: {resultado}")

main()
