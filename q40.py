def conta_maiores_que_10(matriz):
    contador = 0
    for linha in matriz:
        for valor in linha:
            if valor > 10:
                contador += 1
    return contador

def main():
    
    matriz = [[0] * 4 for _ in range(4)]

    for i in range(4):
        for j in range(4):
            matriz[i][j] = float(input(f"Digite o valor para a posição [{i+1}][{j+1}]: "))

    quantidade_maiores_que_10 = conta_maiores_que_10(matriz)

    print(f"\nA matriz possui {quantidade_maiores_que_10} valores maiores que 10.")

main()
