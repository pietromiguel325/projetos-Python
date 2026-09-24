from random import randint
# 1 
def listar_chamados():
    for chamado in chamados:
        print(f"ID: {chamado['id']}")
        print(f"Cliente: {chamado['cliente']}")
        print(f"Categoria: {chamado['categoria']}")
        print(f"Prioridade: {chamado['prioridade']}")
        print(f"Descrição: {chamado['descricao']}")
        print(f"Status: {chamado['status']}")
        print("-"*30)

# 2
def buscar_chamado(id_buscar):
    for chamado in chamados:
        if chamado['id'] == id_buscar:
            return chamado
        
# função auxiliar
def verificar_id(id_buscar):
    while True:
        if id_buscar.isdigit() and int(id_buscar) > 0 and int(id_buscar) <= 100:
            return int(id_buscar)
        else:
            id_buscar = input("Digite o id Novamente (0-100): ")

# função auxiliar
def mostrar_chamado(chamado):
    print("-"*30)
    print(f"ID: {chamado['id']}")
    print(f"Cliente: {chamado['cliente']}")
    print(f"Categoria: {chamado['categoria']}")
    print(f"Prioridade: {chamado['prioridade']}")
    print(f"Descrição: {chamado['descricao']}")
    print(f"Status: {chamado['status']}")
    print("-"*30)

# função auxiliar
def verificar_buscar(chamado, funcao=None):
    if chamado:
        print("Chamado Encontrado!")
        if funcao:
            funcao(chamado)
        mostrar_chamado(chamado)
    else:
        print("Chamado Não Encontado!")

# 3
def cadastrar_chamado(cliente, categoria, prioridade, descricao):
    novo_chamado = dict()
    if chamados:
        ids_existentes = [c['id'] for c in chamados]
        id_novo = randint(1, 100)
        while id_novo in ids_existentes:
            id_novo = randint(1, 100)
    else:
        id_novo = 1
    novo_chamado['id'] = id_novo
    novo_chamado['cliente'] = cliente
    novo_chamado['categoria'] = categoria
    novo_chamado['prioridade'] = prioridade
    novo_chamado['descricao'] = descricao
    novo_chamado['status'] = "Aberto"
    chamados.append(novo_chamado)
    return novo_chamado

# 4
def alterar_status(chamado):
    opcoes = {1: "Aberto", 2: "Em andamento", 3: "Resolvido"}
    for k, v in opcoes.items():
        print(f"{k}- {v}")
    status = input("Escolha uma das opções: ")
    while True:
        if status.isdigit() and int(status) in opcoes:
            status = int(status)
            break
        else:
            status = input("Por Favor! Escolha uma das opções: ")

    if chamado['status'] == opcoes[status]:
        print(f"Erro! O status já está {chamado['status']}")
    else:
        chamado['status'] = opcoes[status]
        print("Status Alterado com Sucesso!")

# 5
def listar_status(status):
    encontrar = False
    for chamado in chamados:
        if chamado['status'].lower() == status.lower():
            mostrar_chamado(chamado)
            encontrar = True
    if not encontrar:
        print(f"\nNenhum status Encontrado!")

# 6
def listar_prioridade(prioridade):
    encontrar = False
    for chamado in chamados:
        if chamado['prioridade'].lower() == prioridade.lower():
            mostrar_chamado(chamado)
            encontrar = True
    if not encontrar:
        print("\nNenhum chamado com essa prioridade")

# 7
def quantidade_categoria():
    categorias = dict()
    for chamado in chamados:
        if chamado['categoria'] not in categorias:
            categorias[chamado['categoria']] = 0
        categorias[chamado['categoria']] += 1
    return categorias

# 8
def quantidade_status():
    status_dict = dict()
    for chamado in chamados:
        if chamado['status'] not in status_dict:
            status_dict[chamado['status']] = 0
        status_dict[chamado['status']] += 1
    return status_dict

# 9
def maior_prioridade():
    prioridades = {"Alta": 3, "Média": 2, "Baixa": 1}
    return max(chamados, key=lambda chamado: prioridades[chamado['prioridade']])

# 10
def mais_chamados():
    clientes = dict()
    for chamado in chamados:
        if chamado['cliente'] not in clientes:
            clientes[chamado['cliente']] = 0
        clientes[chamado['cliente']] += 1
    return max(clientes.items(), key=lambda cliente: cliente[1])

chamados = [
    {"id": 1, "cliente": "João", "categoria": "Hardware", "prioridade": "Alta", "descricao": "Computador não liga", "status": "Aberto"},
    {"id": 2, "cliente": "Maria", "categoria": "Software", "prioridade": "Média", "descricao": "Erro ao abrir sistema", "status": "Em andamento"},
    {"id": 3, "cliente": "Carlos", "categoria": "Rede", "prioridade": "Alta", "descricao": "Sem acesso à internet", "status": "Resolvido"},
    {"id": 4, "cliente": "Ana", "categoria": "Software", "prioridade": "Baixa", "descricao": "Dúvida sobre sistema", "status": "Aberto"},
    {"id": 5, "cliente": "Pedro", "categoria": "Hardware", "prioridade": "Média", "descricao": "Teclado com defeito", "status": "Aberto"},
    {"id": 6, "cliente": "Carlos", "categoria": "Rede", "prioridade": "Média", "descricao": "Cabo da Internet", "status": "Resolvido"}
]

while True:
    print("\n==== MENU CHAMADOS ====")
    print("1 - Listar Chamados")
    print("2 - Buscar Chamado")
    print("3 - Novo Chamado")
    print("4 - Alterar Status")
    print("5 - Listar por Status")
    print("6 - Listar por Prioridade")
    print("7 - Quantidade por Categoria")
    print("8 - Quantidade por Status")
    print("9 - Chamado de Maior Prioridade")
    print("10 - Cliente com Mais Chamados")
    print("0 - Sair")
    opcao = input("Escolha uma das opções: ").strip()
    print()
    match opcao:
        case "0":
            break
        case "1":
            # 1
            listar_chamados()
        case "2":
            # 2
            id_digitado = input("Digite o id do chamado (0-100): ")
            # verificar_buscar(buscar_chamado(verificar_id(id_digitado)))
            id_verificado = verificar_id(id_digitado)
            chamado = buscar_chamado(id_verificado)
            verificar_buscar(chamado)
        case "3":
            # 3 
            cliente = input("Digite o nome do cliente: ").strip().capitalize()
            categoria = input("Digite a categoria: ").strip().capitalize()
            prioridade = input("Digite a prioridade: ").strip().capitalize()
            descricao = input("Digite a descrição: ").strip().capitalize()
            mostrar_chamado(cadastrar_chamado(cliente, categoria, prioridade, descricao))
        case "4":
            # 4
            print("--- ALTERAR STATUS ---")
            id_digitado = input("Digite o id do chamado (0-100): ")
            id_verificado = verificar_id(id_digitado)
            chamado = buscar_chamado(id_verificado)
            verificar_buscar(chamado, alterar_status)
        case "5":
            # 5 
            print("--- LISTAR STATUS ---")
            print("Opções\nAberto\nEm andamento\nResolvido")
            status = str(input("Digite o status: ")).strip()
            listar_status(status)
        case "6":
            # 6
            print("--- LISTAR PRIORIDADE ---")
            print("Opções\nAlta\nMédia\nBaixa")
            prioridade = str(input("Digite a prioridade: ")).strip()
            listar_prioridade(prioridade)
        case "7":
            # 7 
            print("--- QUANTIDADE POR CATEGORIA ---")
            categorias = quantidade_categoria()
            for k, v in categorias.items():
                print(f"{k}: {v}")
        case "8":
            # 8
            print("--- QUANTIDADE POR STATUS ---")
            status_quant = quantidade_status()
            for k, v in status_quant.items():
                print(f"{k}: {v}")
        case "9":
            # 9
            print("--- MAIOR PRIORIDADE ---")
            urgente = maior_prioridade()
            mostrar_chamado(urgente)
        case "10":
            print("--- CLIENTE COM MAIS CHAMADOS ---")
            cliente_mais_chamados = mais_chamados()
            print(f"{cliente_mais_chamados[0]}: {cliente_mais_chamados[1]}")
        case _:
            print("Por Favor! Escolha uma das Opções!")