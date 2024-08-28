
A = []
B = []

for i in range(5):
    while True:
        valor = float(input(f"Digite o valor {i+1} do vetor A: "))
        A.append(valor)
        break


for i in range(5):
    while True:
        valor = float(input(f"Digite o valor {i+1} do vetor B: "))
        B.append(valor)
        break


produto_escalar = 0
for i in range(5):
    produto_escalar += A[i] * B[i]


print("Vetor A:", A)
print("Vetor B:", B)
print("Produto Escalar:", produto_escalar)
