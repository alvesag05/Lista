
vetor_original = [0.0] * 10
vetor_quadrado = [0.0] * 10

print("Digite os 10 números reais:")
for i in range(10):
    vetor_original[i] = float(input("Digite o número {}: ".format(i+1)))

for i in range(10):
    vetor_quadrado[i] = vetor_original[i] ** 2


print("Vetor original:")
for valor in vetor_original:
    print(valor)

print("Vetor com os quadrados:")
for valor in vetor_quadrado:
    print(valor)