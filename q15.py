
vetor = []

for i in range(20):
    valor = int(input(f"Digite o valor {i+1}: "))
    vetor.append(valor)

vetor_sem_repetidos = list(set(vetor))


print("Vetor original:", vetor)
print("Vetor sem repetidos:", vetor_sem_repetidos)
