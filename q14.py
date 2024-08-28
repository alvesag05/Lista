
vetor = []


for i in range(10):
    valor = int(input(f"Digite o valor {i+1}: "))
    vetor.append(valor)


valores_iguais = []
for i in range(len(vetor)):
    for j in range(i+1, len(vetor)):
        if vetor[i] == vetor[j]:
            valores_iguais.append(vetor[i])


print("Vetor:", vetor)
if valores_iguais:
    print("Valores iguais:", valores_iguais)
else:
    print("Não há valores iguais no vetor.")
