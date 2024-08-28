aluno_mais_baixo = None
altura_mais_baixa = float('inf')
aluno_mais_alto = None
altura_mais_alta = float('-inf')

for i in range(10):
    while True:
        aluno = int(input(f"Digite o número do aluno {i+1}: "))
        altura = float(input(f"Digite a altura do aluno {i+1} em metros: "))
        
        
        if altura < altura_mais_baixa:
            altura_mais_baixa = altura
            aluno_mais_baixo = aluno
        
        
        if altura > altura_mais_alta:
            altura_mais_alta = altura
            aluno_mais_alto = aluno
        
        break


print("Aluno mais baixo:", aluno_mais_baixo, "com altura de", altura_mais_baixa, "metros")
print("Aluno mais alto:", aluno_mais_alto, "com altura de", altura_mais_alta, "metros")
