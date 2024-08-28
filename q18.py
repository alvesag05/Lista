
vetor = []


for i in range(10):
    valor = int(input(f"Digite o valor {i+1}: "))
    vetor.append(valor)


x = int(input("Digite o valor de x: "))


multiplos = [valor for valor in vetor if valor % x == 0]


print("Vetor original:", vetor)
print("Múltiplos de", x, ":", multiplos)
print("Quantidade de múltiplos:", len(multiplos))
