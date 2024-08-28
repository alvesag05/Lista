
vetor = [None] * 100

contador = 0

indice = 0

while indice < 100:
    
    contador += 1
    
    
    if contador % 7!= 0 and str(contador)[-1]!= '7':
        
        vetor[indice] = contador
        indice += 1

print("Vetor:", vetor)
