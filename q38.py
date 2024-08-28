def insere_em_ordem(vetor, valor):
    
    i = len(vetor) - 1
    while i >= 0 and vetor[i] > valor:
        vetor[i + 1] = vetor[i]
        i -= 1
    vetor[i + 1] = valor

def main():
    tamanho = 10
    vetor = [0] * tamanho

    for i in range(tamanho):
        valor = float(input(f"Digite o {i + 1}º valor numérico: "))
        insere_em_ordem(vetor, valor)
    
    print("\nValores em ordem crescente:")
    for valor in vetor:
        print(valor, end=" ")
main()
