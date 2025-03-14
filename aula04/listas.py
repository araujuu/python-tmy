# %%

idades = [21, 42, 68, 23, 38]

print(idades)
# %%

julia = ["julia", "araujo", 21, "solteira", 1700]
print(julia)

type(julia)

julia[3]

# %%

# idade
print(julia[2])

# renda
print(julia[4])
# %%

idades = [21, 42, 68, 23, 38, 43]
print("soma das idades: ", sum(idades))

print("quantidade idades: ", len(idades))

print("media das idades: ", sum(idades) / len(idades))

print("menor idade: ", min(idades))

print("maior idade: ", max(idades))
# %%

julia = ["julia araujo", 21, True, "solteira", ["Nilda", "Valdir", "Carol"] ]
len(julia)
julia[4][0]

# %%

julia = ["julia araujo", 21, True, "solteira", ["Nilda", "Valdir", "Carol"], [700, 1700, 4000, 5100, 10000] ]

salario = julia[5]

### video python - Listas - 55:51
# %%
