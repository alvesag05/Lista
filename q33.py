def le_vetor(tamanho):
    vetor = []
    for i in range(tamanho):
        numero = int(input(f"Digite o {i + 1}º número do vetor: "))
        vetor.append(numero)
    return vetor

def compacta_vetor(vetor):
    
    vetor_compactado = [num for num in vetor if num != 0]
    return vetor_compactado

def main():
    tamanho = 15
    
    print("Digite os elementos do vetor:")
    vetor = le_vetor(tamanho)
    
    vetor_compactado = compacta_vetor(vetor)
    
    print("\nVetor original:", vetor)
    print("Vetor compactado:", vetor_compactado)

main()
