def le_vetor(tamanho):
    vetor = []
    for i in range(tamanho):
        numero = float(input(f"Digite o {i + 1}º número real: "))
        vetor.append(numero)
    return vetor

def ordena_vetor(vetor):
    return sorted(vetor)

def main():
    tamanho = 10
    
    print("Digite os elementos do vetor:")
    vetor = le_vetor(tamanho)
    
    vetor_ordenado = ordena_vetor(vetor)
    
    print("\nVetor ordenado:", vetor_ordenado)

main()
