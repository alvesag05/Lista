
valores = []


for i in range(5):
    valor = float(input(f"Digite o valor {i+1}: "))
    valores.append(valor)


max_valor = max(valores)
min_valor = min(valores)
media_valor = sum(valores) / len(valores)


print("Valores:", valores)
print("Valor máximo:", max_valor)
print("Valor mínimo:", min_valor)
print("Valor médio:", media_valor)
