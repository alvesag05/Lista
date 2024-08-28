def main():

    matriz_alunos = [
        [1001, 7, 8, 0],
        [1002, 6, 7, 0],
        [1003, 8, 9, 0],
        [1004, 5, 6, 0],
        [1005, 7, 8, 0]
    ]

    maior_nota_final = -1
    matricula_maior_nota = -1
    soma_notas_finais = 0
    
    for aluno in matriz_alunos:
        matricula = aluno[0]
        media_provas = aluno[1]
        media_trabalhos = aluno[2]
        
        nota_final = media_provas + media_trabalhos
        
        aluno[3] = nota_final
        
        if nota_final > maior_nota_final:
            maior_nota_final = nota_final
            matricula_maior_nota = matricula
        
        soma_notas_finais += nota_final
    
    num_alunos = len(matriz_alunos)
    media_notas_finais = soma_notas_finais / num_alunos

    print(f"Matrícula do aluno com maior nota final: {matricula_maior_nota}")
    print(f"Média aritmética das notas finais: {media_notas_finais:.2f}")

main()
