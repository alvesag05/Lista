def soma_colunas(matriz):
   
    soma_coluna = [0] * len(matriz[0]) 
    
    for col in range(len(matriz[0])):
       
        for lin in range(len(matriz)):
            soma_coluna[col] += matriz[lin][col]
    
    return soma_coluna

def main():
  
    matriz = [[0] * 3 for _ in range(3)]

    print("Digite os elementos da matriz 3x3:")
    for i in range(3):
        for j in range(3):
            matriz[i][j] = int(input(f"Digite o elemento [{i}][{j}]: "))

    resultado = soma_colunas(matriz)
    
    print("\nSoma das colunas da matriz:")
    print(resultado)

main()
