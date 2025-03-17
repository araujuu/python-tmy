# %%
lista = [2, 132, "julia", ["js", "python", "node"], True]

lista[2]
# %%

### dicionarios são pares de chave/valor

dados_julia = {"nome":"Julia", 
               "Sobrenome":"Araujo", 
               "filhos":False, 
               "formacao":["Ciencia da computação", "DataScience"],
               "Cargo":[{"nome":"Desenvolvedor", "Empresa":"Globo"},
                        {"nome":"Engenheira De Machine Learning", "Empresa":"IBM"},
                        {"nome": "Engenheira De RAP", "Empresa": "Google"}]}

print(dados_julia)
# %%

dados_julia["formacao"][-1]
dados_julia["Cargo"][-1]["Empresa"]
# %%

dados_julia["estado civil"] = "solteira"

print(dados_julia)
# %%

print("Chaves: ", dados_julia.keys())

print("Valores: ", dados_julia.values())

print("itens: ", dados_julia.items())
# %%

for i in dados_julia:
    print(i, dados_julia[i])
# %%

### print(chave, "->", dados_julia[chave])

#/ for item in dados_julia.items():
#/   print(item)

for chave, valor in dados_julia.items():
    print(chave, "->", valor)

# %%
##### tuplas

lista = [23,34,26,43,12,24]
dados_julia
dados_julia['salario'] = "3194.23"
dados_julia
# %%

tupla_julia = [21, 0, 'solteira', 'dev']
tupla_julia
tupla_julia.append("ana caratina")
tupla_julia
# %%
