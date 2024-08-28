
valores = []


for i in range(5):
    valor = float(input(f"Digite o valor {i+1}: "))
    valores.append(valor)


max_pos = valores.index(max(valores)) + 1
min_pos = valores.index(min(valores)) + 1


print("Valores:", valores)
print(f"O maior valor está na posição {max_pos}")
print(f"O menor valor está na posição {min_pos}")
