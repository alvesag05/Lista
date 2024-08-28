
vetor = []


for i in range(10):
    valor = int(input(f"Digite o valor {i+1}: "))
    vetor.append(valor)


for i in range(len(vetor)):
    if vetor[i] < 0:
        vetor[i] = 0


print("Vetor original:", vetor)
print("Vetor com valores negativos substituídos por 0:", vetor)
