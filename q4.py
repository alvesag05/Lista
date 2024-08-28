
vetor = [0] * 8


print("Digite os 8 valores do vetor:")
for i in range(8):
    vetor[i] = int(input("Digite o valor {}: ".format(i+1)))

x = int(input("Digite a posição X (1-8): ")) - 1
y = int(input("Digite a posição Y (1-8): ")) - 1


if x < 0 or x >= 8 or y < 0 or y >= 8:
    print("Posição inválida!")
else:
   
    soma = vetor[x] + vetor[y]
    print("A soma dos valores encontrados nas posições X e Y é:", soma)