def numero_para_vetor(numero):
    vetor = []
    while numero > 0:
        vetor.append(numero % 10)
        numero //= 10
    
    if not vetor:
        vetor.append(0) 
    return vetor

def soma_vetores(vetor_a, vetor_b):
    max_len = max(len(vetor_a), len(vetor_b))
    vetor_soma = []
    carry = 0

    for i in range(max_len):
        digito_a = vetor_a[i] if i < len(vetor_a) else 0
        digito_b = vetor_b[i] if i < len(vetor_b) else 0

        soma = digito_a + digito_b + carry
        if soma >= 10:
            carry = 1
            soma -= 10
        else:
            carry = 0
        
        vetor_soma.append(soma)

    if carry > 0:
        vetor_soma.append(carry)

    return vetor_soma

def main():
    a = int(input("Digite um número positivo menor que 10000 para a: "))
    b = int(input("Digite um número positivo menor que 10000 para b: "))

    if a < 0 or a >= 10000 or b < 0 or b >= 10000:
        print("Os números devem ser positivos e menores que 10000.")
        return

    vetor_a = numero_para_vetor(a)
    vetor_b = numero_para_vetor(b)

    vetor_soma = soma_vetores(vetor_a, vetor_b)

    print("Vetor de a:", vetor_a)
    print("Vetor de b:", vetor_b)
    print("Vetor da soma de a e b:", vetor_soma)

main()
