from colorama import Fore, Style

def check_number(sorteio, usuario):
    if sorteio == usuario:
        print(Fore.GREEN + "Parabens, você acertou!" + Style.RESET_ALL)
        return True

    elif sorteio < usuario:
        print("numero muito alto :( tente um numero menor")

    else:
        print("numero muito baixo :( tente um numero maior")

        return False

