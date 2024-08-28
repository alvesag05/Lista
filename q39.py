def triangulo_de_pascal(n):
    triangulo = []
    for linha in range(n):
        linha_atual = []
        for coluna in range(linha + 1):
            if coluna == 0 or coluna == linha:
                linha_atual.append(1)
            else:
                anterior_superior_esquerdo = triangulo[linha - 1][coluna - 1]
                anterior_superior_direito = triangulo[linha - 1][coluna]
                linha_atual.append(anterior_superior_esquerdo + anterior_superior_direito)
        triangulo.append(linha_atual)
    return triangulo

def main():
    n = int(input("Digite um número inteiro positivo n: "))
    
    if n <= 0:
        print("O número precisa ser positivo.")
        return
    
    resultado = triangulo_de_pascal(n)
    
    print(f"\nTriângulo de Pascal com {n} linhas:")
    for linha in resultado:
        print(' '.join(map(str, linha)))

main()
