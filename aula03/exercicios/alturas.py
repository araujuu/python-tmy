# %%

soma = 0
quantidade_valor = 0

while quantidade_valor < 4:
    altura = input("entre com a altura: ")
    altura = float(altura)
    soma += altura
    quantidade_valor += 1
    
print("soma das alturas: ", soma)
# %%

# soma = 0  # valor final

# quant_entradas = 4 # contador de entrada

# while quant_entradas > 0:
#     altura = input("entre com a altura: ")
#     altura = float(altura)
#     soma += altura
#     quant_entradas -= 1
# print("soma das alturas: ", soma)