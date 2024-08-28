import math

v = [None] * 10

for i in range(10):
    while True:
        valor = float(input(f"Digite o valor {i+1} do vetor: "))
        v[i] = valor
        break

m = sum(v) / len(v)

desvio_padrao = math.sqrt(sum((x - m) ** 2 for x in v) / len(v))

print("Desvio Padrão:", desvio_padrao)
