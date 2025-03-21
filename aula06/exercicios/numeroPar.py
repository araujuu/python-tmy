# %%

numero = int(input("Digite um número para saber se ele é par ou impar: "))

def par_impar():
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

print("o valor", numero, "é",par_impar())
par_impar()
# %%
