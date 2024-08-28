
vetor = []


for i in range(5):
    valor = float(input(f"Digite o valor {i+1}: "))
    vetor.append(valor)


codigo = int(input("Digite o código (0 para sair, 1 para ordem direta, 2 para ordem inversa): "))

if codigo == 0:
    print("Programa finalizado.")
elif codigo == 1:
    print("Vetor na ordem direta:", vetor)
elif codigo == 2:
    print("Vetor na ordem inversa:", vetor[::-1])
else:
    print("Código inválido. Tente novamente!")
