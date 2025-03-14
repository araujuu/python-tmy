soma = 0
entradas = 4

for i in range(entradas):
    altura = input("Digite sua altura: ")
    altura = float(altura)
    soma += altura

print("Soma das alturas: ", soma)