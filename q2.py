
valores = []

for i in range(6):
    valor = int(input("Digite o valor {}: ".format(i+1)))
    valores.append(valor)


print("Os valores que você digitou são:")
for valor in valores:
    print(valor)