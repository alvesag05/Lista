
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
    if i % 2 == 0:
        C.append(A[i//2])
    else:
        C.append(B[i//2])


print("Vetor C:")
for i in range(0, len(C), 2):
    print(C[i:i+2])
