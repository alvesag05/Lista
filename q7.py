
vetor = [0] * 10


print("Digite os 10 valores do vetor:")
for i in range(10):
    vetor[i] = int(input("Digite o valor {}: ".format(i+1)))


print("Vetor:", vetor)


maior = max(vetor)
posicao_maior = vetor.index(maior) + 1

print("O maior elemento do vetor é:", maior)
print("Ele se encontra na posição", posicao_maior)