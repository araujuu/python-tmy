# %%

fruta = input("Digite uma fruta: ")

frutas = {"Pera":"R$1,25",
             "Goiaba":"R$2,15",
            "Abacaxi":"R$3,20",
            "Jaca":"R$5,80",
            "Laranja":"R$0,65",
            "Limão":"R$1,25",
            "Maça":"R$1,50",
            "Banana":"R$2,75",
            "Uva":"R$1,50"
            }

if fruta in frutas:
    print(frutas[fruta])
else:
    print("entre com um valor valido")

#### dica, em vez de usar muitos if's else's, use dicionarios como o exemplo acima.
#  E utilize um unico if para nao ter erro de Key e o programa quebrar
# %%
