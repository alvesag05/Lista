def le_vetor(tamanho, nome_vetor):
    vetor = []
    for i in range(tamanho):
        numero = int(input(f"Digite o {i + 1}º número do vetor {nome_vetor}: "))
        vetor.append(numero)
    return vetor

def soma_vetores(vetor1, vetor2):
    return [vetor1[i] + vetor2[i] for i in range(len(vetor1))]

def produto_vetores(vetor1, vetor2):
    return [vetor1[i] * vetor2[i] for i in range(len(vetor1))]

def diferenca_vetores(vetor1, vetor2):
    return [num for num in vetor1 if num not in vetor2]

def intersecao_vetores(vetor1, vetor2):
    return [num for num in vetor1 if num in vetor2]

def uniao_vetores(vetor1, vetor2):
    uniao = list(vetor1)  
    for num in vetor2:
        if num not in vetor1:
            uniao.append(num)
    return uniao

def main():
    tamanho = 5
    
    print("Digite os elementos do vetor x:")
    vetor_x = le_vetor(tamanho, 'x')
    
    print("\nDigite os elementos do vetor y:")
    vetor_y = le_vetor(tamanho, 'y')
    
    soma = soma_vetores(vetor_x, vetor_y)
    produto = produto_vetores(vetor_x, vetor_y)
    diferenca = diferenca_vetores(vetor_x, vetor_y)
    intersecao = intersecao_vetores(vetor_x, vetor_y)
    uniao = uniao_vetores(vetor_x, vetor_y)
    
    print("\nSoma entre x e y:", soma)
    print("Produto entre x e y:", produto)
    print("Diferença entre x e y:", diferenca)
    print("Interseção entre x e y:", intersecao)
    print("União entre x e y:", uniao)

main()
