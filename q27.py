def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


vetor = [None] * 10


for i in range(10):
    while True:
        valor = int(input(f"Digite o valor {i+1} do vetor: "))
        vetor[i] = valor
        break


primos = [(i, x) for i, x in enumerate(vetor) if eh_primo(x)]


print("Elementos primos e suas posições no vetor:")
for pos, primo in primos:
    print(f"Posição {pos+1}: {primo}")
