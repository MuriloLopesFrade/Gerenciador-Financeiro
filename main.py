transacao = []

def menu():

    while True:

        print("\n<========== Bem vindo ao seu gerenciador financeiro ==========>")
        print("\n1- Cadastrar receita;")
        print("2- Cadastrar de despesa;")
        print("3- Listagem de transação;")
        print("4- Verificar saldo")
        print("5- Sair")

        try:
            op = int(input("\nDigite uma opção:"))
        except ValueError:
            print("Digite um número válido.")
            continue

        if op == 1:
            cadastro_transacao("Receita")
        elif op == 2:
            cadastro_transacao("Despesa")
        elif op == 3:
            listagem_transacao()
        elif op == 4:
            verifica_saldo()
        elif op == 5:
            print("\nSaindo do Sistema")
            break
        else:
            print("\nOpção invalida!")


def cadastro_transacao(tipo):
    descricao = input("Descrição:")

    try:
        valor = float(input("Valor:"))
    except ValueError:
        print("Valor inválido!")
        return

    data = input("Data: ")

    transacao.append(
        {
            "descrição": descricao,
            "tipo": tipo,
            "valor": valor,
            "data": data
        }
    )

    print(f"{tipo.capitalize()} cadastro com sucesso!")

def listagem_transacao():

        print("\n====> Listagem de transação:")
        print("\n1- listar total de transações")
        print("2- apenas receitas")
        print("3- apenas despesas")

        try:
            op= int(input("\nSelecione uma opção: "))
        except ValueError:
            print("Valor inválido!")
            return

        if op == 1:
            lista = transacao
        elif op == 2:
            lista = [t for t in transacao if t["tipo"] == "Receita"]
        elif op == 3:
            lista = [t for t in transacao if t["tipo"] == "Despesa"]
        else:
            print("\nOpção inválida!")
            return

        if not lista:
            print("Nenhuma transação encontrada")

        print("\n====> TRANSAÇÕES")
        for t in lista:
            print(f"{t['data']} | {t['descrição']} | {t['tipo']} | {t['valor']}")


def verifica_saldo():
    saldo = 0

    for t in transacao:
        if t['tipo'] == "Receita":
            saldo +=t['valor']
        else:
            saldo -= t['valor']

    print(f"Saldo total: R${round(saldo, 2)}")


menu()