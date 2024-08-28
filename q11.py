
vetor = [0.0] * 10


print("Digite os 10 números reais do vetor:")
for i in range(10):
    vetor[i] = float(input("Digite o valor {}: ".format(i+1)))


negativos = sum(1 for x in vetor if x < 0)


positivos = sum(x for x in vetor if x > 0)


print("Quantidade de números negativos:", negativos)
print("Soma dos números positivos:", positivos)