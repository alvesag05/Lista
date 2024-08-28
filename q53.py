import random

def gerar_cartela():
    numeros_disponiveis = list(range(100))
    random.shuffle(numeros_disponiveis)
    
    cartela = []
    index = 0
    
    for _ in range(5):
        linha = numeros_disponiveis[index:index+5]
        cartela.append(linha)
        index += 5
    
    return cartela

def exibir_cartela(cartela):
    for linha in cartela:
        print(linha)

def main():

    cartela = gerar_cartela()
    
    print("Cartela de Bingo:")
    exibir_cartela(cartela)

main()
