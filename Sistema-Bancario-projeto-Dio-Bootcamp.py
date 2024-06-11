
print("░B░e░n░v░i░n░d░o░ ░a░o░ ░S░e░u░ ░B░a░n░c░o░")
# Menu de opções
menu = """
█▓▒░⡷⠂[D]⠐⢾░▒▓█ ░D░e░p░o░s░i░t░a░r░
█▓▒░⡷⠂[S]⠐⢾░▒▓█ ░S░a░c░a░r░
█▓▒░⡷⠂[E]⠐⢾░▒▓█ ░E░x░t░r░a░t░o░
█▓▒░⡷⠂[Q]⠐⢾░▒▓█ ░S░a░i░r░

░=░>░ """

# Variáveis iniciais
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"░D░e░p░ó░s░i░t░o░: R$ {valor:.2f}\n"
        print(f"░D░e░p░ó░s░i░t░o░ de R$ {valor:.2f} ░r░e░a░l░i░z░a░d░o░ ░c░o░m░ ░s░u░c░e░s░s░o░!░")
    else:
        print("░O░p░e░r░a░ç░ã░o░ ░f░a░l░h░o░u░!░ ░O░ ░v░a░l░o░r░ ░i░n░f░o░r░m░a░d░o░ ░é░ ░i░n░v░á░l░i░d░o░.░")
    return saldo, extrato


def sacar(valor, saldo, extrato, numero_saques, LIMITE_SAQUES, limite):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("░O░p░e░r░a░ç░ã░o░ ░f░a░l░h░o░u░!░ ░V░o░c░ê░ ░n░ã░o░ ░t░e░m░ ░s░a░l░d░o░ ░s░u░f░i░c░i░e░n░t░e░.░")
    elif excedeu_limite:
        print("░O░p░e░r░a░ç░ã░o░ ░f░a░l░h░o░u░!░ ░O░ ░v░a░l░o░r░ ░d░o░ ░s░a░q░u░e░ ░e░x░c░e░d░e░ ░o░ ░l░i░m░i░t░e░.░")
    elif excedeu_saques:
        print("░O░p░e░r░a░ç░ã░o░ ░f░a░l░h░o░u░!░ ░N░ú░m░e░r░o░ ░m░á░x░i░m░o░ ░d░e░ ░s░a░q░u░e░s░ ░e░x░c░e░d░i░d░o░.░")
    elif valor > 0:
        saldo -= valor
        extrato += f"░S░a░q░u░e░:░ R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"░S░a░q░u░e░:░ ░d░e░ R$ {valor:.2f} ░r░e░a░l░i░z░a░d░o░ ░c░o░m░ ░s░u░c░e░s░s░o░!░")
    else:
        print("░O░p░e░r░a░ç░ã░o░ ░f░a░l░h░o░u░!░ ░O░ ░v░a░l░o░r░ ░i░n░f░o░r░m░a░d░o░ ░é░ ░i░n░v░á░l░i░d░o░.░")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n█▓▒░⡷⠂================⠐⢾░▒▓█ ⫷ 𝔼𝕩𝕥𝕣𝕒𝕥𝕠 ⫸ █▓▒░⡷⠂================⠐⢾░▒▓█")
    print("░N░ã░o░ ░f░o░r░a░m░ ░r░e░a░l░i░z░a░d░a░s░ ░m░o░v░i░m░e░n░t░a░ç░õ░e░s░.░" if not extrato else extrato)
    print(f"\n░S░a░l░d░o░:░ R$ {saldo:.2f}")
    print("█▓▒░⡷⠂===========================================================⠐⢾░▒▓█")


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("░I░n░f░o░r░m░e░ ░o░ ░v░a░l░o░r░ ░d░o░ ░d░e░p░ó░s░i░t░o░:░ "))
        saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao == "s":
        valor = float(input("░I░n░f░o░r░m░e░ ░o░ ░v░a░l░o░r░ ░d░o░ ░s░a░q░u░e░:░ "))
        saldo, extrato, numero_saques = sacar(valor, saldo, extrato, numero_saques, LIMITE_SAQUES, limite)

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "q":
        print("░O░b░r░i░g░a░d░o░ ░p░o░r░ ░u░s░a░r░ ░n░o░s░s░o░ ░s░i░s░t░e░m░a░ ░b░a░n░c░á░r░i░o░.░ ░A░t░é░ ░l░o░g░o░!░")
        break

    else:
        print("░O░p░e░r░a░ç░ã░o░ ░i░n░v░á░l░i░d░a░,░ ░p░o░r░ ░f░a░v░o░r░ ░s░e░l░e░c░i░o░n░e░ ░n░o░v░a░m░e░n░t░e░ ░a░ "
              "░o░p░e░r░a░ç░ã░o░ ░d░e░s░e░j░a░d░a░.░")
