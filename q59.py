def main():

    matriz = [
        [1.5, 2.5, 3.5, 4.5, 5.5, 6.5],
        [7.5, 8.5, 9.5, 10.5, 11.5, 12.5],
        [13.5, 14.5, 15.5, 16.5, 17.5, 18.5]
    ]

    soma_colunas_impares = 0
    for linha in matriz:
        soma_colunas_impares += linha[0] + linha[2] + linha[4]
    print(f"Soma dos elementos das colunas ímpares: {soma_colunas_impares}")
    
    soma_segunda_coluna = 0
    soma_quarta_coluna = 0
    for linha in matriz:
        soma_segunda_coluna += linha[1]
        soma_quarta_coluna += linha[3]
    media_colunas_2_4 = (soma_segunda_coluna + soma_quarta_coluna) / len(matriz)
    print(f"Média aritmética das colunas 2 e 4: {media_colunas_2_4}")
    
    for linha in matriz:
        linha[5] = linha[1] + linha[2]
    
    print("Matriz modificada:")
    for linha in matriz:
        print(linha)

main()

