
vetor = [0] * 10


print("Digite os 10 valores do vetor:")
for i in range(10):
    vetor[i] = int(input("Digite o valor {}: ".format(i+1)))

maior = max(vetor)
menor = min(vetor)

# Imprima o resultado
print("O maior elemento do vetor é:", maior)
print("O menor elemento do vetor é:", menor)