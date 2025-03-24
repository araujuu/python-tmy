# %%
nome_arquivo = "historia.txt"

with open(nome_arquivo) as open_file:
    conteudo = open_file.read()


### ao inves de fazer isso tudo abaixo, faça o de cima,
### que é a mesma coisa    








### abre o arquivo em formato de leitura
open_file = open(nome_arquivo)
# %%

print(open_file)
# %%

### lê os dados do arquivo
conteudo = open_file.read()
print(conteudo)

# %%

### fecha o arquivo
open_file.close()
# %%
