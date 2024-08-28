def soma_diagonal_secundaria(matriz):
    soma = 0
    tamanho = len(matriz)
    
    for i in range(tamanho):
        soma += matriz[i][tamanho - 1 - i] 
    
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
    
    
    resultado = soma_diagonal_secundaria(matriz)
    
   
    print("\nMatriz 3x3:")
    for linha in matriz:
        print(linha)
    
   
    print(f"\nA soma dos elementos da diagonal secundária é: {resultado}")

main()
