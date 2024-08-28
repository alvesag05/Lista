def determinar_piores_notas(matriz_notas):
    num_alunos = len(matriz_notas)
    num_provas = len(matriz_notas[0])
    
    piores_notas_prova1 = 0
    piores_notas_prova2 = 0
    piores_notas_prova3 = 0
    
    for aluno in matriz_notas:
        pior_nota = min(aluno)
        
        if aluno[0] == pior_nota:
            piores_notas_prova1 += 1
        elif aluno[1] == pior_nota:
            piores_notas_prova2 += 1
        elif aluno[2] == pior_nota:
            piores_notas_prova3 += 1
    
    return piores_notas_prova1, piores_notas_prova2, piores_notas_prova3

def main():

    matriz_notas = [
        [7, 8, 6],
        [5, 6, 7],
        [8, 6, 5],
        [6, 7, 8],
        [7, 5, 6],
        [6, 5, 7],
        [8, 7, 6],
        [5, 6, 7],
        [7, 8, 6],
        [6, 7, 8]
    ]
    
    piores_prova1, piores_prova2, piores_prova3 = determinar_piores_notas(matriz_notas)
    
    print(f"Número de alunos com pior nota na prova 1: {piores_prova1}")
    print(f"Número de alunos com pior nota na prova 2: {piores_prova2}")
    print(f"Número de alunos com pior nota na prova 3: {piores_prova3}")

main()
