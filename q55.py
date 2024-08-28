def calcular_nota(gabarito, respostas_aluno):
    nota = 0
    for i in range(len(gabarito)):
        if respostas_aluno[i] == gabarito[i]:
            nota += 1
    return nota

def main():
    
    gabarito = ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']
    
    alunos = [
        {'matricula': 1, 'respostas': ['a', 'b', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']},
        {'matricula': 2, 'respostas': ['b', 'a', 'c', 'd', 'e', 'a', 'b', 'c', 'd', 'e']},
        {'matricula': 3, 'respostas': ['c', 'b', 'a', 'd', 'e', 'a', 'b', 'c', 'd', 'e']}
    ]
    
    for aluno in alunos:
        matricula = aluno['matricula']
        respostas_aluno = aluno['respostas']
    
        nota = calcular_nota(gabarito, respostas_aluno)
        
        print(f"Matrícula: {matricula}")
        print(f"Respostas do aluno: {respostas_aluno}")
        print(f"Nota: {nota}\n")

    num_alunos = len(alunos)
    aprovados = sum(1 for aluno in alunos if calcular_nota(gabarito, aluno['respostas']) >= 7)
    percent_aprovacao = (aprovados / num_alunos) * 100
    
    print(f"Percentual de aprovação: {percent_aprovacao:.2f}%")

main()
