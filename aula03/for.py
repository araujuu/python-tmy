nome = "Julia Almeida"

for letra in nome:
    print(letra)


numero = 2
numero_max = 100

for i in range(1, numero_max+1):
    print(numero, "x", i, "=", numero *i)


for i in range(4, 101):
    if i % 4 == 0:
        print(i)