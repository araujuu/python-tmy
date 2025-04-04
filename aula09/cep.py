# %%
import requests
import json
import pandas as pd

endereco = input("Digite seu CEP (somente números): ")

url = f"https://viacep.com.br/ws/{endereco}/json/"
resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()

    if "erro" in dados:
        print("CEP inválido! Tente novamente.")
    else:
        print("Seu CEP é:", dados)

        with open("ceps.json", "w", encoding="utf-8") as open_file:
            json.dump(dados, open_file, ensure_ascii=False, indent=4)

        dataset = pd.DataFrame([dados])
        print(dataset)
else:
    print("Erro ao conectar com o serviço. Tente novamente mais tarde.")


#### aula 12 - dados api (30:30) 

# %%


