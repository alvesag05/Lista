
notas = [0] * 15


print("Digite as notas dos 15 alunos:")
for i in range(15):
    notas[i] = float(input("Digite a nota do aluno {}: ".format(i+1)))


media_geral = sum(notas) / len(notas)

print("A média geral é:", media_geral)