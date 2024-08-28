def main():

    matriz1 = ler_matriz(2, 2)
    matriz2 = ler_matriz(2, 2)
    
    opcao = ''
    
    while opcao != 'e':
       
        print("\n===== MENU =====")
        print("a) Somar as duas matrizes")
        print("b) Subtrair a primeira matriz da segunda")
        print("c) Adicionar uma constante às duas matrizes")
        print("d) Imprimir as matrizes")
        print("e) Sair do programa")
        
        opcao = input("Escolha uma opção (a, b, c, d ou e): ").lower()
        
        if opcao == 'a':
           
            resultado = somar_matrizes(matriz1, matriz2)
            print("Resultado da soma das matrizes:")
            imprimir_matriz(resultado)
        
        elif opcao == 'b':
        
            resultado = subtrair_matrizes(matriz2, matriz1)
            print("Resultado da subtração da primeira matriz pela segunda:")
            imprimir_matriz(resultado)
        
        elif opcao == 'c':
            
            constante = float(input("Digite a constante a ser adicionada às matrizes: "))
            adicionar_constante(matriz1, constante)
            adicionar_constante(matriz2, constante)
            print(f"Matriz 1 com constante {constante} adicionada:")
            imprimir_matriz(matriz1)
            print(f"Matriz 2 com constante {constante} adicionada:")
            imprimir_matriz(matriz2)
        
        elif opcao == 'd':
      
            print("Matriz 1:")
            imprimir_matriz(matriz1)
            print("Matriz 2:")
            imprimir_matriz(matriz2)
        
        elif opcao == 'e':
            print("Encerrando o programa...")
        
        else:
            print("Opção inválida. Escolha novamente.")

def ler_matriz(num_linhas, num_colunas):
    
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            elemento = float(input(f"Digite o elemento [{i+1}][{j+1}]: "))
            linha.append(elemento)
        matriz.append(linha)
    return matriz

def somar_matrizes(matriz1, matriz2):
    
    resultado = []
    for i in range(2):
        linha = []
        for j in range(2):
            soma = matriz1[i][j] + matriz2[i][j]
            linha.append(soma)
        resultado.append(linha)
    return resultado

def subtrair_matrizes(matriz1, matriz2):
   
    resultado = []
    for i in range(2):
        linha = []
        for j in range(2):
            subtracao = matriz1[i][j] - matriz2[i][j]
            linha.append(subtracao)
        resultado.append(linha)
    return resultado

def adicionar_constante(matriz, constante):

    for i in range(2):
        for j in range(2):
            matriz[i][j] += constante

def imprimir_matriz(matriz):
    
    for linha in matriz:
        print(linha)

main()
