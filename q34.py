def le_numeros_unicos(tamanho):
    vetor = []
    while len(vetor) < tamanho:
        numero = int(input(f"Digite um número único ({len(vetor) + 1}/{tamanho}): "))
        if numero in vetor:
            print("Número já digitado. Por favor, digite outro número.")
        else:
            vetor.append(numero)
    return vetor

def main():
    tamanho = 10
    
    print("Digite 10 números diferentes:")
    vetor = le_numeros_unicos(tamanho)
    
    print("\nVetor final:", vetor)

main()
