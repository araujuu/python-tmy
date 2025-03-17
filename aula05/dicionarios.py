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
