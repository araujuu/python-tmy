# %% 
from get_input import *
from colorama import Fore, Style
import random
from check_number import *

numero_sorteio = random.randint(1, 15)

for i in range(3):
    numero_usuario = get_input()
    acertou = check_number(numero_sorteio, numero_usuario)

    if acertou:
        break

else:
    print(Fore.BLUE + "suas tentativas acabaram" + Style.RESET_ALL)


# %%
