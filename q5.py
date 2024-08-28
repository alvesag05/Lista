
vetor = [0] * 10

print("Digite os 10 valores do vetor:")
for i in range(10):
    vetor[i] = int(input("Digite o valor {}: ".format(i+1)))


contagem_pares = 0
for valor in vetor:
    if valor % 2 == 0:
        contagem_pares += 1


print("O vetor possui", contagem_pares, "valores pares.")