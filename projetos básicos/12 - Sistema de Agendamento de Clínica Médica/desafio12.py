from random import randint
# 1
def listar_agendamentos():
    print("-"*30)
    for agendamento in agendamentos:
        print(f"ID: {agendamento['id']}")
        print(f"Paciente: {agendamento['paciente']}")
        print(f"Médico: {agendamento['medico']}")
        print(f"Especialidade: {agendamento['especialidade']}")
        print(f"Valor: R${agendamento['valor']:.2f}")
        print(f"Status: {agendamento['status']}")
        print("-"*30)

# 2
def verificar_id(id_agendamento):
    while True:
        if id_agendamento.isdigit() and int(id_agendamento) <= 100:
            id_agendamento = int(id_agendamento)
            break
        else:
            id_agendamento = input("Digite o id novamento (0-100): ").strip()
    return id_agendamento

def buscar_agendamento(id_verificado):
    for agendamento in agendamentos:
        if agendamento['id'] == id_verificado:
            return agendamento

def mostrar_agendamento(agendamento):
    print("-"*30)
    print(f"ID: {agendamento['id']}")
    print(f"Paciente: {agendamento['paciente']}")
    print(f"Médico: {agendamento['medico']}")
    print(f"Especialidade: {agendamento['especialidade']}")
    print(f"Valor: R${agendamento['valor']:.2f}")
    print(f"Status: {agendamento['status']}")
    print("-"*30)

def verificar_busca(agendamento, funcao=None):
    if agendamento:
        print("Agendamento Encontrado com Sucesso!")
        if funcao:
            funcao(agendamento)
        mostrar_agendamento(agendamento)
    else:
        print("Agendamento Não Encontrado!")

# 3
def cadastrar_agendamento(paciente, medico, especialidade, valor):
    novo_agendamento = dict()
    if agendamentos:
        id_existentes = [agendamento['id'] for agendamento in agendamentos]
        id_novo = randint(1,100)
        while id_novo in id_existentes:
            id_novo = randint(1,100)
    else:
        id_novo = 1
    novo_agendamento['id'] = id_novo
    novo_agendamento['paciente'] = paciente
    novo_agendamento['medico'] = medico
    novo_agendamento['especialidade'] = especialidade
    novo_agendamento['valor'] = valor
    novo_agendamento['status'] = "Agendado"
    agendamentos.append(novo_agendamento)
    return novo_agendamento

# 4
def alterar_status(agendamento):
    opcoes = {
        1: "Agendado",
        2: "Realizado",
        3: "Cancelado"
    }
    for k, v in opcoes.items():
        print(f"{k} - {v}")
    status = input("Escolha uma das opções: ")
    while True:
        if status.isdigit() and int(status) in opcoes:
            status = int(status)
            break
        else:
            status = input("Por Favor! Escolha uma das opções: ")
    if agendamento['status'] == opcoes[status]:
        print(f"Não pode mudar {agendamento['status']}(atual) -> {opcoes[status]}(novo)")
    else:
        print(f"Status alterado com Sucesso! {agendamento['status']}(atual) -> {opcoes[status]}(novo)")
        agendamento['status'] = opcoes[status]

# 5
def verificar_status(status):
    status_permitidos = ['agendado', 'realizado', 'cancelado']
    while status.lower() not in status_permitidos:
        print("\nPor Favor! Digite uma das Opções: ")
        for permitidos in status_permitidos:
                print(f"{permitidos.capitalize()}")
        status = input("Digite novamente o status: ").strip()
    return status

def listar_status(status_verificado):
    encontrou = False
    for agendamento in agendamentos:
        if agendamento['status'].lower() == status_verificado.lower():
            mostrar_agendamento(agendamento)
            encontrou = True
    if not encontrou:
        print(f"Nenhum agendamento com o status '{status_verificado}'.")

# 6
def listar_especialidade(especialidade):
    encontrou = False
    for agendamento in agendamentos:
        if agendamento['especialidade'].lower() == especialidade:
            mostrar_agendamento(agendamento)
            encontrou = True
    if not encontrou:
        print(f"Nenhum agendamento com a especialidade {especialidade}")

#7
def faturamento_realizado():
    soma = 0
    for agendamento in agendamentos:
        if agendamento['status'] == "Realizado":
            soma += agendamento['valor']
    return soma

# 8
def quantidade_por_medicos():
    medico = dict()
    for agendamento in agendamentos:
        if agendamento['medico'] not in medico:
            medico[agendamento['medico']] = 0
        medico[agendamento['medico']] += 1
    return medico

# 9
def maior_consulta(agendamentos):
    return max(agendamentos, key=lambda ag: ag['valor'])

# 10
def medico_mais_consulta():
    consultas = dict()
    for agendamento in agendamentos:
        if agendamento['medico'] not in consultas:
            consultas[agendamento['medico']] = 0
        consultas[agendamento['medico']] += 1
    return max(consultas.items(), key=lambda consul: consul[1])

# 11
def pacientes_mais_consulta():
    consultas = dict()
    for agendamento in agendamentos:
        if agendamento['paciente'] not in consultas:
            consultas[agendamento['paciente']] = 0
        consultas[agendamento['paciente']] += 1
    return max(consultas.items(), key=lambda com: com[1])

agendamentos = [
    {"id": 1, "paciente": "João", "medico": "Dr. Carlos", "especialidade": "Cardiologia", "valor": 350, "status": "Agendado"},
    {"id": 2, "paciente": "Maria", "medico": "Dra. Ana", "especialidade": "Dermatologia", "valor": 250, "status": "Realizado"},
    {"id": 3, "paciente": "Carlos", "medico": "Dr. Carlos", "especialidade": "Cardiologia", "valor": 350, "status": "Cancelado"},
    {"id": 4, "paciente": "Ana", "medico": "Dr. João", "especialidade": "Ortopedia", "valor": 300, "status": "Agendado"},
    {"id": 5, "paciente": "Carlos", "medico": "Dra. Ana", "especialidade": "Dermatologia", "valor": 250, "status": "Realizado"},
    {"id": 6, "paciente": "Mariana", "medico": "Dr. João", "especialidade": "Ortopedia", "valor": 300, "status": "Agendado"}
]

while True:
    print("\n=== MENU CLÍNICA ===")
    print("1 - Listar Agendamento")
    print("2 - Buscar Agendamento")
    print("3 - Novo Agendamento")
    print("4 - Alterar Staus")
    print("5 - Listar por Status")
    print("6 - Listar por Especialidade")
    print("7 - Faturamento Completo")
    print("8 - Quantidade de Médicos Por Consulta")
    print("9 - Maior Agendamento")
    print("10 - Médico com mais Consultas")
    print("11 - Paciente com mais Consultas")
    opcao = input("Escolha uma das opções: ")
    print()
    match opcao:
        case "0":
            break
        case "1":
            print("--- LISTA DOS AGENDAMENTOS ---")
            listar_agendamentos()
        case "2":
            print("--- BUSCA CHAMADO ---")
            id_agendamento = input("Digite o id do agendamento (0-100): ").strip()
            id_verificado = verificar_id(id_agendamento)
            agendamento = buscar_agendamento(id_verificado)
            verificar_busca(agendamento)
        case "3":
            print("--- CADASTRAR AGENDAMENTO ---")
            paciente = input("Digite o nome do Paciente: ").strip().capitalize()
            medico = input("Digite o nome do Médico: ").strip().title()
            especialidade = input("Digite a Especialidade: ").strip().capitalize()
            while True:
                try:
                    valor = input("Digite o valor do agendamento: ")
                    valor = float(valor)
                    if valor > 0:
                        break
                    else:
                        print("O valor deve ser MAIOR que 0! ")
                except ValueError:
                    print("Só aceita valor numérico!")           
            novo_agendamento = cadastrar_agendamento(paciente, medico, especialidade, valor)
            mostrar_agendamento(novo_agendamento)
        case "4":
            print("--- ALTERAR STATUS ---")
            id_agendamento = input("Digite o id do agendamento (0-100): ").strip()
            id_verificado = verificar_id(id_agendamento)
            agendamento = buscar_agendamento(id_verificado)
            verificar_busca(agendamento, alterar_status)
        case "5":
            print("--- LISTA POR STATUS ---")
            print("OPÇÕES:")
            print("Agendado\nRealizado\nCancelado")
            status = input("Digite o status: ").strip()
            status_verificado = verificar_status(status)
            listar_status(status_verificado)
        case "6":
            print("--- LISTA ESPECIALIDADE ---")
            especialidade_existentes = {agendamento['especialidade'].lower() for agendamento in agendamentos}
            while True:
                print("OPÇÕES: ")
                for esp in especialidade_existentes:
                    print(esp.capitalize())   
                especialidade = input("Digite a Especialidade: ").strip().lower()
                if especialidade in especialidade_existentes:
                    break
                else:
                    print("\nESCOLHA UMA DAS OPÇÕES!")
            listar_especialidade(especialidade)
        case "7":
            print("--- FATURAMENTO TOTAL ---")
            faturamento = faturamento_realizado()
            print(f"R${faturamento:.2f}")
        case "8":
            print("--- QUANTIDADE DE MÉDICOS POR CONSULTA ---")
            medicos = quantidade_por_medicos()
            for k, v in medicos.items():
                print(f"{k}: {v}")
        case "9":
            print("--- MAIOR AGENDAMENTO ---")
            maior_valor = maior_consulta(agendamentos)
            for k, v in maior_valor.items():
                print(f"{k.capitalize()}: {v}")
        case "10":
            print("--- MÉDICO COM MAIS CONSULTAS ---")
            medico = medico_mais_consulta()
            print(f"{medico[0]}: {medico[1]}")
        case "11":
            print("--- PACIENTE COM MAIS CONSULTAS ---")
            paciente = pacientes_mais_consulta()
            print(f"{paciente[0]}: {paciente[1]}")
        case _:
            print("Por Favor! Selecione uma das Opções!")
    