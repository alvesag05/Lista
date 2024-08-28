def ordena_vetor_misto(vetor):
    
    for i in range(1, 6):
        chave = vetor[i]
        j = i - 1
        while j >= 0 and vetor[j] > chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave
    
    for i in range(7, 11):
        chave = vetor[i]
        j = i - 1
        while j >= 6 and vetor[j] < chave:
            vetor[j + 1] = vetor[j]
            j -= 1
        vetor[j + 1] = chave
    
    return vetor

vetor_A = [1, 2, 3, 4, 5, 6, 11, 10, 9, 8, 7]

vetor_A_ordenado = ordena_vetor_misto(vetor_A)

print("Vetor A ordenado:", vetor_A_ordenado)
