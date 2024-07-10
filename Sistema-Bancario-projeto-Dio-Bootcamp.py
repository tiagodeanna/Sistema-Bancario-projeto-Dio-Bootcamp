import textwrap

class Banco:
    def __init__(self):
        self.usuarios = []
        self.contas = []
        self.AGENCIA = "0001"
        self.LIMITE_SAQUES = 3

    def menu_inicial(self):
        # Menu de opções
        menu_inicial = """\n
        ============ MENU ==============
        █▓▒░⡷⠂[ D ]⠐⢾░▒▓█\t ░D░e░p░o░s░i░t░a░r░
        █▓▒░⡷⠂[ S ]⠐⢾░▒▓█\t ░S░a░c░a░r░
        █▓▒░⡷⠂[ E ]⠐⢾░▒▓█\t ░E░x░t░r░a░t░o░
        █▓▒░⡷⠂[N C]⠐⢾░▒▓█\t ░N░O░V░A░ ░C░O░N░T░A░
        █▓▒░⡷⠂[L C]⠐⢾░▒▓█\t ░L░I░S░T░A░R ░C░O░N░T░A░S░ 
        █▓▒░⡷⠂[N U]⠐⢾░▒▓█\t ░N░O░V░O░ ░U░S░U░Á░R░I░O░
        █▓▒░⡷⠂[ Q ]⠐⢾░▒▓█\t ░S░a░i░r░

        ░=░>░ """
        return input(textwrap.dedent(menu_inicial))

    def criar_usuario(self):
        cpf = input("░I░N░F░O░R░M░E░ ░o░ ░C░P░F░ (░S░O░M░E░N░T░E ░N░U░M░E░R░O░S░): ")
        usuario = self.filtrar_usuario(cpf)

        if usuario:
            print("░J░Á░ ░E░X░I░S░T░E░ ░U░S░U░Á░R░I░O ░C░O░M░ ░E░S░S░E░ ░C░P░F░!")
            return
        
        nome = input("░I░N░F░O░R░M░E░ ░O░ ░N░O░M░E░ ░C░O░M░P░L░E░T░O░: ")
        data_nascimento = input("░I░N░F░O░R░M░E░ ░A░ ░D░A░T░A░ ░D░E░ ░N░A░S░C░I░M░E░N░T░O░ (░D░D░-░M░M░-░A░A░A░A░): ")
        endereco = input("░I░N░F░O░R░M░E░ ░O░ ░E░N░D░E░R░E░Ç░O░ (░L░A░R░G░A░D░O░U░R░O░, ░N░R░O░ - ░B░A░I░R░R░O░ - ░C░I░D░A░D░E░/░S░I░G░L░A░ ░E░S░T░A░D░O░): ")

        self.usuarios.append(Usuario(nome, data_nascimento, cpf, endereco))
        print("░░===░U░s░u░á░r░i░o░ ░c░r░i░a░d░o░ ░c░o░m░ ░s░u░c░e░s░s░o░!░===░░")

    def filtrar_usuario(self, cpf):
        usuarios_filtrados = [usuario for usuario in self.usuarios if usuario.cpf == cpf]
        return usuarios_filtrados[0] if usuarios_filtrados else None

    def criar_conta(self):
        cpf = input("░I░N░F░O░R░M░E░ ░O░ ░C░P░F░ ░D░O░ ░U░S░U░A░R░I░O░: ")
        usuario = self.filtrar_usuario(cpf)

        if usuario:
            numero_conta = len(self.contas) + 1
            self.contas.append(Conta(self.AGENCIA, numero_conta, usuario))
            print("░░===░C░o░n░t░a░ ░c░r░i░a░d░a░ ░c░o░m░ ░s░u░c░e░s░s░o░!░===░░")
        else:
            print("░U░s░u░á░r░i░o░ ░n░ã░o░ ░e░n░c░o░n░t░r░a░d░o░,░ ░c░a░d░a░s░t░r░o░ ░n░ã░o░ ░r░e░a░l░i░z░a░d░o░.░")

    def listar_contas(self):
        for conta in self.contas:
            linha = f"""\
                Agência:\t{conta.agencia}
                C/C:\t\t{conta.numero_conta}
                Titular:\t{conta.usuario.nome}
            """
            print("=" * 100)
            print(textwrap.dedent(linha))

    def main(self):
        saldo = 0
        limite = 500
        extrato = ""
        numero_saques = 0

        while True:
            opcao = self.menu_inicial()

            if opcao == "D":
                valor = float(input("░I░n░f░o░r░m░e░ ░o░ ░v░a░l░o░r░ ░d░o░ ░d░e░p░ó░s░i░t░o░: "))
                saldo, extrato = Deposito().executar(saldo, valor, extrato)

            elif opcao == "S":
                valor = float(input("░I░n░f░o░r░m░e░ ░o░ ░v░a░l░o░r░ ░d░o░ ░s░a░q░u░e░: "))
                saldo, extrato = Saque().executar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    limite=limite,
                    numero_saques=numero_saques,
                    LIMITE_SAQUES=self.LIMITE_SAQUES,
                )

            elif opcao == "E":
                ExibirExtrato().executar(saldo, extrato=extrato)

            elif opcao == "N U":
                self.criar_usuario()

            elif opcao == "N C":
                self.criar_conta()

            elif opcao == "L C":
                self.listar_contas()

            elif opcao == "Q":
                break

            else:
                print("░O░p░ç░ã░o░ ░i░n░v░á░l░i░d░a░,░ ░t░e░n░t░e░ ░n░o░v░a░m░e░n░t░e░.░")


class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco


class Conta:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario


class OperacaoBancaria:
    def executar(self, *args, **kwargs):
        raise NotImplementedError("Subclasses devem implementar este método")


class Deposito(OperacaoBancaria):
    def executar(self, saldo, valor, extrato):
        if valor > 0:
            saldo += valor
            extrato += f"░D░e░p░ó░s░i░t░o░: R$ {valor:.2f}\n"
            print(f"░D░e░p░ó░s░i░t░o░ de R$ {valor:.2f} ░r░e░a░l░i░z░a░d░o░ ░c░o░m░ ░s░u░c░e░s░s░o░!░")
        else:
            print("░O░p░e░r░a░ç░ã░o░ ░f░a░l░h░o░u░!░ ░O░ ░v░a░l░o░r░ ░i░n░f░o░r░m░a░d░o░ ░é░ ░i░n░v░á░l░i░d░o░.░")
        return saldo, extrato


class Saque(OperacaoBancaria):
    def executar(self, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
        if valor > saldo:
            print("░O░p░e░r░a░ç░ã░o░ ░f░a░l░h░o░u░!░ ░S░a░l░d░o░ ░i░n░s░u░f░i░c░i░e░n░t░e░.░")
        elif valor > limite:
            print("░O░p░e░r░a░ç░ã░o░ ░f░a░l░h░o░u░!░ ░O░ ░v░a░l░o░r░ ░d░o░ ░s░a░q░u░e░ ░e░x░c░e░d░e░ ░o░ ░l░i░m░i░t░e░.░")
        elif numero_saques >= LIMITE_SAQUES:
            print("░O░p░e░r░a░ç░ã░o░ ░f░a░l░h░o░u░!░ ░N░ú░m░e░r░o░ ░m░á░x░i░m░o░ ░d░e░ ░s░a░q░u░e░s░ ░e░x░c░e░d░i░d░o░.░")
        elif valor > 0:
            saldo -= valor
            extrato += f"░S░a░q░u░e░: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"░S░a░q░u░e░ de R$ {valor:.2f} ░r░e░a░l░i░z░a░d░o░ ░c░o░m░ ░s░u░c░e░s░s░o░!░")
        else:
            print("░O░p░e░r░a░ç░ã░o░ ░f░a░l░h░o░u░!░ ░O░ ░v░a░l░o░r░ ░i░n░f░o░r░m░a░d░o░ ░é░ ░i░n░v░á░l░i░d░o░.░")
        return saldo, extrato


class ExibirExtrato(OperacaoBancaria):
    def executar(self, saldo, extrato):
        print("\n================= EXTRATO =================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===========================================")


if __name__ == "__main__":
    banco = Banco()
    banco.main()
