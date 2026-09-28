from random import randint

# 1

def listar_funcionarios():
    for funcionario in funcionarios:
        print(f"ID: {funcionario['id']}")
        print(f"Nome: {funcionario['nome']}")
        print(f"Cargo: {funcionario['cargo']}")
        print(f"Setor: {funcionario['setor']}")
        print(f"Salário: R${funcionario['salario']:.2f}")
        print(f"Ativo: {funcionario['ativo']}")
        print("-"*30)


# 2

def buscar_funcionario(id_funcionario):
    for funcionario in funcionarios:
        if funcionario['id'] == id_funcionario:
            return funcionario


# Funções auxiliares

def mostrar_funcionario(funcionario):
    print("-"*30)
    print(f"ID: {funcionario['id']}")
    print(f"Nome: {funcionario['nome']}")
    print(f"Cargo: {funcionario['cargo']}")
    print(f"Setor: {funcionario['setor']}")
    print(f"Salário: R${funcionario['salario']:.2f}")
    print(f"Ativo: {funcionario['ativo']}")
    print("-"*30)


def verificar_busca(funcionario, funcao=None):
    if funcionario:
        print("Funcionário Encontrado!")

        if funcao:
            funcao(funcionario)

        mostrar_funcionario(funcionario)

    else:
        print("Funcionário Não Encontrado!")


# Funções auxiliares

def verifica_id(id_entrada):
    while True:
        if id_entrada.isdigit() and int(id_entrada) > 0 and int(id_entrada) <= 100:
            id_entrada = int(id_entrada)
            break
        else:
            id_entrada = input("Por Favor! Digite um id válido: ")

    return id_entrada


def verifica_sal():
    while True:
        try:
            salario = input("Digite o salário: ").strip().replace(",", ".")
            salario = float(salario)

            if salario > 0:
                break
            else:
                print("Erro! Salário deve ser maior que 0")

        except ValueError:
            print("Erro! Digite Números Válidos!")

    return salario


# 3

def cadastrar_funcionario(nome, cargo, setor, salario, ativo=True):
    novo_funcionario = dict()

    if funcionarios:
        ids_usados = [func['id'] for func in funcionarios]

        id_novo = randint(1, 100)

        while id_novo in ids_usados:
            id_novo = randint(1, 100)

    else:
        id_novo = 1

    novo_funcionario['id'] = id_novo
    novo_funcionario['nome'] = nome
    novo_funcionario['cargo'] = cargo
    novo_funcionario['setor'] = setor
    novo_funcionario['salario'] = salario
    novo_funcionario['ativo'] = ativo

    funcionarios.append(novo_funcionario)

    return novo_funcionario


# 4

def alterar_salario(funcionario):
    novo_salario = verifica_sal()

    if funcionario['ativo']:
        funcionario['salario'] = novo_salario
        print("\nSalário Alterado com Sucesso!")

    else:
        print("\nSalário Não Pode ser Alterado!")


# 5

def demitir_funcionario(funcionario):
    if not funcionario['ativo']:
        print("Funcionário já está demitido!")

    else:
        funcionario['ativo'] = False
        print("Funcionário demitido!")


# 6

def listar_ativos():
    for funcionario in funcionarios:
        if funcionario['ativo']:
            mostrar_funcionario(funcionario)


# 7 

def quantidade_func_setor():
    setores = dict()

    for funcionario in funcionarios:
        setor_padronizado = funcionario['setor'].lower()

        if funcionario['ativo']:
            if setor_padronizado not in setores:
                setores[setor_padronizado] = 0

            setores[setor_padronizado] += 1

    return setores


# 8 

def folha_salarial():
    soma = 0

    for funcionario in funcionarios:
        if funcionario['ativo']:
            soma += funcionario['salario']

    return soma


# 9 

def maior_salario():
    ativos = [f for f in funcionarios if f['ativo']]

    if ativos:
        funcionario_maior = max(
            ativos,
            key=lambda funcionario: funcionario['salario']
        )

        print(f"{funcionario_maior['nome']}: R${funcionario_maior['salario']:.2f}")

    else:
        print("Nenhum funcionário ativo no momento!")


# 10

def media_salarial_setor():
    setor_completo = dict()

    # 1. ACÚMULO DE DADOS

    # Passa por cada funcionário da lista para juntar as somas e as quantidades
    for funcionario in funcionarios:

        # Pega o setor em minúsculo para não duplicar 'TI' e 'ti'
        setor_padrao = funcionario['setor'].lower()

        # Considera apenas funcionários ativos
        if funcionario['ativo']:

            # Se é a primeira vez que esse setor aparece, cria a estrutura zerada
            if setor_padrao not in setor_completo:
                setor_completo[setor_padrao] = {"soma_salario": 0,"quantidade": 0} # Ex: {'ti': {"soma_salario": 0, "quantidade": 0}}

            # Soma o salário do funcionário atual no total do setor dele
            setor_completo[setor_padrao]["soma_salario"] += funcionario["salario"]

            # Soma +1 na contagem de funcionários desse setor
            setor_completo[setor_padrao]["quantidade"] += 1

    # 2. CÁLCULO DA MÉDIA

    # Passa por cada setor criado acima:
    # 'setor' é a chave (ex: 'ti')
    # 'dados' é o dicionário interno (ex: {"soma_salario": 11500, "quantidade": 3})
    # O resultado fica: {'ti': soma_salario / quantidade}
    media = {
        setor: dados['soma_salario'] / dados['quantidade']
        for setor, dados in setor_completo.items()
    }

    return media


funcionarios = [
    {"id": 1, "nome": "João", "cargo": "Desenvolvedor", "setor": "TI", "salario": 4500.00, "ativo": True},
    {"id": 2, "nome": "Maria", "cargo": "Analista", "setor": "Financeiro", "salario": 3800.00, "ativo": True},
    {"id": 3, "nome": "Carlos", "cargo": "Desenvolvedor", "setor": "TI", "salario": 5200.00, "ativo": False},
    {"id": 4, "nome": "Ana", "cargo": "Gerente", "setor": "RH", "salario": 6500.00, "ativo": True},
    {"id": 5, "nome": "Pedro", "cargo": "Analista", "setor": "Financeiro", "salario": 4100.00, "ativo": True},
    {"id": 6, "nome": "Lucas", "cargo": "Estagiário", "setor": "TI", "salario": 1800.00, "ativo": True},
]


while True:

    print("\n=== SISTEMA DE FUNCIONÁRIOS ===")
    print("1 - Listar Funcionários")
    print("2 - Buscar Funcinário")
    print("3 - Cadastrar Funcionário")
    print("4 - Alterar Salário")
    print("5 - Demitir Funcionário")
    print("6 - Funcionários Ativos")
    print("7 - Quantidade de Funcionários por Setor")
    print("8 - Folha Salarial")
    print("9 - Funcionário com Maior Salário")
    print("10 - Média Salarial por Setor")
    print("0 - Sair")

    opcao = input("Escolha uma das opções: ").strip()
    print()

    match opcao:

        case "0":
            break

        case "1":
            print("--- LISTA DOS FUNCIONÁRIOS ---")
            listar_funcionarios()

        case "2":
            print("--- BUSCAR FUNCIONÁRIO ---")

            id_buscar = input("Digite o id do funcionário (0-100): ")
            print()

            id_verificado = verifica_id(id_buscar)
            funcionario = buscar_funcionario(id_verificado)

            verificar_busca(funcionario)

        case "3":
            print("--- CADASTRAR FUNCIONÁRIO ---")

            nome = input("Digite o nome do funcionário: ").strip().capitalize()
            cargo = input("Digite o cargo: ").strip().capitalize()
            setor = input("Digite o setor: ").strip().capitalize()

            salario = verifica_sal()

            novo_funcionario = cadastrar_funcionario(
                nome,
                cargo,
                setor,
                salario
            )

            print("\nFuncionário Cadastrado Com Sucesso!")
            mostrar_funcionario(novo_funcionario)

        case "4":
            print("--- ALTERAR SALARIO ---")

            id_buscar = input("Digite o id do funcionário: ")

            id_verificado = verifica_id(id_buscar)
            funcionario = buscar_funcionario(id_verificado)

            verificar_busca(funcionario, alterar_salario)

        case "5":
            print("--- DEMITIR FUNCIONÁRIO ---")

            id_buscar = input("Digite o id do funcionário (0-100): ")
            print()

            id_verificado = verifica_id(id_buscar)
            funcionario = buscar_funcionario(id_verificado)

            verificar_busca(funcionario, demitir_funcionario)

        case "6":
            print("--- FUNCIONÁRIOS ATIVOS ---")
            listar_ativos()

        case "7":
            print("--- QUANTIDADE DE FUNCIONÁRIOS POR SETOR ---")

            funcionario_setor = quantidade_func_setor()

            for k, v in funcionario_setor.items():
                print(f"{k.upper()}: {v}")

        case "8":
            print("--- FOLHA SALARIAL ---")

            soma_salarial = folha_salarial()

            print(f"R${soma_salarial:.2f}")

        case "9":
            print("--- MAIOR SALÁRIO ---")
            maior_salario()

        case "10":
            print("--- MEDIA SALARIAL POR SETOR ---")

            media = media_salarial_setor()

            for k, v in media.items():
                print(f"{k.upper()}: R${v:.2f}")

        case _:
            print("ERRO! SELECIONE UMA DAS OPÇÕES!")