
A = []
B = []
C = []


for i in range(10):
    while True:
        valor = int(input(f"Digite o valor {i+1} do vetor A: "))
        A.append(valor)
        break


for i in range(10):
    while True:
        valor = int(input(f"Digite o valor {i+1} do vetor B: "))
        B.append(valor)
        break


for i in range(10):
    C.append(A[i] - B[i])


print("Vetor C:")
for i in range(0, len(C), 2):
    print(C[i:i+2])
