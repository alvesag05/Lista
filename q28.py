
v = [None] * 10

for i in range(10):
    while True:
        valor = int(input(f"Digite o valor {i+1} do vetor: "))
        v[i] = valor
        break

v1 = []
v2 = []


for valor in v:
    if valor % 2 == 0:
        v2.append(valor)
    else:
        v1.append(valor)

print("Elementos ímpares de v1:")
for valor in v1:
    print(valor)

print("\nElementos pares de v2:")
for valor in v2:
    print(valor)
