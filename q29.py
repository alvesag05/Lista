
def processa_numeros():
    numeros = []

    for i in range(6):
        numero = int(input(f"Digite o {i + 1}º número inteiro: "))
        numeros.append(numero)

    pares = []
    impares = []

    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    soma_pares = sum(pares)

    print("\nNúmeros pares digitados:", pares)
    print("Soma dos números pares digitados:", soma_pares)
    print("Números ímpares digitados:", impares)
    print("Quantidade de números ímpares digitados:", len(impares))

processa_numeros()
