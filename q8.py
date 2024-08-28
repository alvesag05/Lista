
vetor = [0] * 6


print("Digite os 6 valores do vetor:")
for i in range(6):
    vetor[i] = int(input("Digite o valor {}: ".format(i+1)))


print("Os valores na ordem inversa são:")
for i in range(5, -1, -1):
    print(vetor[i])