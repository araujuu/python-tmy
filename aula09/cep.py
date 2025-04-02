# %%
import requests
import json


endereco = input("Digite seu CEP: ")

url = f"https://viacep.com.br/ws/{endereco}/json/" 
resposta = requests.get(url)


if resposta.status_code == 200:
    dados = resposta.json()
    print("Seu CEP é:", dados)

    with open("ceps.json", "w", encoding="utf-8") as open_file:
        json.dump(dados, open_file, ensure_ascii=False, indent=4)

else:
    print("CEP invalido!, tente novamente")

#### aula 12 - dados api (30:30) 

# %%


