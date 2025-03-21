# %%
def calcImposto(preco:float, taxa_base:0.3, **kwargs):
    imposto = preco * taxa_base

    for i in kwargs:  
        print(i, kwargs[i])
        imposto += preco * kwargs[i]

    return imposto
# %%

impostos_gerais = {

    "municipio" : 0.01, 
    "estadual" : 0.005, 
    "nacional" : 0.0001
}

calcImposto(100, 0.3 **impostos_gerais)

# %%
