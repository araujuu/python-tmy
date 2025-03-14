# %%

saldoTotal = 0

while True:
    saldo = input("Digite o saldo da conta: ")
    if saldo == "":
        break

    saldoTotal += float(saldo)
print("Saldo da conta total: ", saldoTotal)