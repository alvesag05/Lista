def le_vetor(tamanho):
    vetor = []
    for i in range(tamanho):
        numero = int(input(f"Digite o {i + 1}º número do vetor: "))
        vetor.append(numero)
    return vetor

def uniao_vetores(vetor1, vetor2):
    
    set1 = set(vetor1)
    set2 = set(vetor2)
    uniao = list(set1 | set2)
    return uniao

def main():
    tamanho = 10
    
    print("Digite os elementos do primeiro vetor:")
    vetor1 = le_vetor(tamanho)
    
    print("\nDigite os elementos do segundo vetor:")
    vetor2 = le_vetor(tamanho)
    
    uniao = uniao_vetores(vetor1, vetor2)
    
    print("\nUnião entre os dois vetores:", uniao)

main()
