# Programa Garrafa d'agua
# Se o cliente escolher agua mineral natural, será cobrado R$ 1,50
# Se o cliente escolher agua mineral com gás, será cobrado R$ 2,50

# texto = """ 

# Escolha sua água para comprar
# (1) Água mineral natural
# (2) Água mineral com gás

# """

# opcao = input(texto)

# conta = 0
# if opcao == '1':
#     conta = 1.50
# elif opcao == '2':
#     conta = 2.50

# if conta == 0:
#     print("Entre com a opção correta, por favor!")
# else:
#     print("Sua conta é R$", conta)









## Programa quantidade agua

texto = """ 

# Escolha sua água para comprar
# (1) Água mineral natural - R$ 1,50
# (2) Água mineral com gás - R$ 2,50

"""

opcao = input(texto)

valor_item = 0
if opcao == '1':
    valor_item = 1.50
elif opcao == '2':
     valor_item = 2.50
if valor_item == 0:
     print("Entre com a opção correta, por favor!")
else:
    quantidade = input("Quantas garrafas?: ")
    quantidade = int(quantidade)
    valor_total = valor_item * quantidade 
    print("Sua conta deu: R$", valor_total)