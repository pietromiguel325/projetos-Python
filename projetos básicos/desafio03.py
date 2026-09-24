# Lista todos os clientes
def listar_clientes():
    for cliente in clientes:
        print(f"Id: {cliente['id']}")
        print(f"Nome: {cliente['nome']}")
        print(f"Email: {cliente['email']}")
        print(f"Idade: {cliente['idade']}")
        print()


# Mostra os dados de um único cliente, tem que receber um dicionário
def mostrar_cliente(cliente):
    print(f"Nome: {cliente['nome']}")
    print(f"Email: {cliente['email']}")
    print(f"Idade: {cliente['idade']}")


# Busca um cliente pelo ID
def buscar_cliente(id_cliente):
    # filter() retorna um objeto filter, por isso usamos list()
    # para transformar o resultado em uma lista.
    #
    # O lambda recebe cada dicionário da lista clientes
    # e verifica se o ID dele é igual ao ID procurado.
    return list(filter(
        lambda cliente: cliente['id'] == id_cliente,
        clientes
    ))


# Cadastra um novo cliente
def cadastrar_cliente():
    novo_cliente = {}

    # Se já existirem clientes, pega o ID do último
    # e soma 1 para gerar o ID do novo cliente.
    if clientes:
        novo_cliente['id'] = clientes[-1]['id'] + 1
    else:
        # Se a lista estiver vazia, começa pelo ID 1.
        novo_cliente['id'] = 1

    # input() já retorna uma string, então não precisamos usar str().
    novo_cliente['nome'] = input("Digite o Nome: ")
    novo_cliente['email'] = input("Digite o Email: ")
    novo_cliente['idade'] = int(input("Digite a Idade: "))

    # Adiciona o novo dicionário à lista de clientes.
    clientes.append(novo_cliente)

    print("Cliente cadastrado com sucesso!")


clientes = [
    {"id": 1, "nome": "João Silva", "email": "joao@email.com", "idade": 25},
    {"id": 2, "nome": "Maria Santos", "email": "maria@email.com", "idade": 31},
    {"id": 3, "nome": "Carlos Oliveira", "email": "carlos@email.com", "idade": 28},
]


while True:
    print("===== SISTEMA DE CLIENTES =====")
    print("1 - Listar clientes")
    print("2 - Buscar cliente")
    print("3 - Cadastrar cliente")
    print("4 - Atualizar cliente")
    print("5 - Excluir cliente")
    print("0 - Sair")

    opcao = int(input("Escolha uma das opções: "))
    print()

    match opcao:

        case 0:
            print("Programa encerrado.")
            break

        case 1:
            listar_clientes()

        case 2:
            buscar = int(input("Digite o ID: "))

            # Retorna uma lista contendo o cliente encontrado.
            cliente_procurado = buscar_cliente(buscar)

            if cliente_procurado:
                print("\nCliente Encontrado:")

                # Como o filter retorna uma lista,
                # usamos [0] para acessar o dicionário.
                mostrar_cliente(cliente_procurado[0])
            else:
                print("Cliente Não Encontrado!")

            print()

        case 3:
            print("==== Cadastro de Clientes ====")
            cadastrar_cliente()
            print()

        case 4:
            alterar = int(input("Digite o ID do Cliente: "))

            # Busca o cliente pelo ID.
            alterar_cliente = buscar_cliente(alterar)

            if alterar_cliente:
                print("Dados Atuais:")

                # [0] acessa o dicionário encontrado.
                mostrar_cliente(alterar_cliente[0])

                print("\nDigite os novos Dados:")

                # Altera os valores do dicionário.
                alterar_cliente[0]['nome'] = input("Novo Nome: ")
                alterar_cliente[0]['email'] = input("Novo Email: ")
                alterar_cliente[0]['idade'] = int(input("Nova Idade: "))

                print("Cliente Atualizado com Sucesso!")

            else:
                print("Cliente Não Encontrado!")

        case 5:
            excluir = int(input(
                "Digite o ID do Cliente que será excluído: "
            ))

            # Busca o cliente que será excluído.
            buscar_excluir = buscar_cliente(excluir)

            if buscar_excluir:
                print("Dados do Cliente:")

                mostrar_cliente(buscar_excluir[0])

                # strip() remove espaços extras.
                # upper() transforma a resposta em maiúscula.
                resp = input(
                    "\nTem certeza que deseja excluir? "
                ).strip().upper()

                # Aceita somente S ou N.
                while resp not in ("S", "N"):
                    resp = input(
                        "Por favor tente novamente! "
                        "Tem certeza que deseja excluir? "
                    ).strip().upper()

                if resp == "S":

                    # remove() recebe o dicionário que queremos
                    # retirar da lista clientes.
                    clientes.remove(buscar_excluir[0])

                    print("Cliente Excluído com Sucesso!")

                else:
                    print("Operação Cancelada!")

            else:
                print("Cliente Não Encontrado!")

        case _:
            print("Operação Inválida! Tente Novamente")