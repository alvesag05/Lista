def calcular_pontuacao(respostas_alunos, gabarito):
    num_alunos = len(respostas_alunos)
    num_questoes = len(gabarito)
    resultado = []
    
    for i in range(num_alunos):
        pontuacao = 0
        for j in range(num_questoes):
            if respostas_alunos[i][j] == gabarito[j]:
                pontuacao += 1
        resultado.append(pontuacao)
    
    return resultado

def main():
    
    respostas_alunos = [
        ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'],
        ['b', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'],
        ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'],
        ['c', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b'],
        ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']
    ]

    gabarito = ['a', 'b', 'c', 'd', 'a', 'b', 'c', 'd', 'a', 'b']
    
    resultado = calcular_pontuacao(respostas_alunos, gabarito)

    for i, pontuacao in enumerate(resultado):
        print(f"Aluno {i+1}: Pontuação = {pontuacao}")

main()
