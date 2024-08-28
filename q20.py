
vetor1 = []
vetor2 = []


for i in range(10):
    while True:
        valor = int(input(f"Digite o valor {i+1} (entre 0 e 50): "))
        if 0 <= valor <= 50:
            vetor1.append(valor)
            break
        else:
            print("Valor inválido. Tente novamente!")


for valor in vetor1:
    if valor % 2!= 0:
        vetor2.append(valor)


print("Vetor 1:")
for i in range(0, len(vetor1), 2):
    print(vetor1[i:i+2])

print("\nVetor 2:")
for i in range(0, len(vetor2), 2):
    print(vetor2[i:i+2])
