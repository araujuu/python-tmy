# %%

def jurosCompostos(aporte=int, taxa=float, anos=int) -> float:

    """jurosCompostos serve para calcular o retorno financeiro a partir de um aporte.
    Deve-se considerar o valor, a taxa de juros atual e o tempo (em anos), para cálculo do juros
    
    aporte: 
        Um número inteiro, que represente o valor em R$
        
    taxa: 
        Um número float entre 0 e 1 que represente o valor da taxa de juros
        
    anos: 
        Um número inteiro >= 1 que representa o tempo que o investimento terá liquidez"""
    
    return aporte * (1 + taxa) ** anos

# %%

jurosCompostos(aporte=1000, taxa=0.13, anos=4)
# %%
