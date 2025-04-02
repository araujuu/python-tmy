from colorama import Fore, Style

def get_input():
    while True:
        try:
            numero_usuario = int(input("Digite um numero entre 1 e 15:\n"))

        except ValueError as err:
            print(Fore.RED + "valor invalido" + Style.RESET_ALL)
            continue

        if 1 <= numero_usuario <= 15:
            return numero_usuario
    
        print(Fore.RED + "valor invalido, o valor deve ser entre 1 e 15" + Style.RESET_ALL)