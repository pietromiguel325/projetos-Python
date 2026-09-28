from random import randint

def listar_pedidos():
    print("\n==== LISTA DE PEDIDOS ====")
    for pedido in pedidos:
        print(f"Id: {pedido['id']}")
        print(f"Cliente: {pedido['cliente']}")
        print(f"Produto: {pedido['produto']}")
        print(f"Categoria: {pedido['categoria']}")
        print(f"Quantidade: {pedido['quantidade']}")
        print(f"Preço: {pedido['preco']:.2f}")
        print(f"Status: {pedido['status']}")
        print("-"*30)

def buscar_pedido(id_pedido):
    for pedido in pedidos:
        if pedido['id'] == id_pedido:
            return pedido

def mostrar_pedido(pedido):
    print()
    print(f"Id: {pedido['id']}")
    print(f"Cliente: {pedido['cliente']}")
    print(f"Produto: {pedido['produto']}")
    print(f"Categoria: {pedido['categoria']}")
    print(f"Quantidade: {pedido['quantidade']}")
    print(f"Preço: {pedido['preco']:.2f}")
    print(f"Status: {pedido['status']}")
    print("-"*30)

def verificar_busca(pedido, funcao=None):
    if pedido:
        print("Pedido Achado!")
        if funcao:
            funcao(pedido)
        mostrar_pedido(pedido)
    else:
        print("Pedido Não Encontrado!")

def criar_pedido(cliente, produto, categoria, quantidade, preco):
    novo_pedido = dict()
    ids_existentes = [pedido['id'] for pedido in pedidos]
    if pedidos:
        id_novo = randint(1, 100)
        while id_novo in ids_existentes:
            id_novo = randint(1, 100)
        novo_pedido['id'] = id_novo
    else:
        novo_pedido['id'] = 1
    novo_pedido['cliente'] = cliente
    novo_pedido['produto'] = produto
    novo_pedido['categoria'] = categoria
    novo_pedido['quantidade'] = quantidade
    novo_pedido['preco'] = preco
    novo_pedido['status'] = "Processando"
    pedidos.append(novo_pedido)
    return novo_pedido

def alterar_status(pedido, status):
    status_opcoes = {1: "Processando", 2: "Enviado", 3: "Entregue", 4: "Cancelado"}
    if status not in status_opcoes:
        print("Erro! Deve selecionar uma das opções!")
        return
    novo_status = status_opcoes[status]
    if pedido['status'] == novo_status:
        print(f"--- Erro Status! Já está {novo_status} ---")
    else:
        pedido['status'] = novo_status
        print("--- Status Alterado com Sucesso! ----")

# Faturamento -> Usado na função 5, 6, 7
def faturamento(pedido): # recebe o pedido (dict) como parâmetro
    return pedido['quantidade'] * pedido['preco']

# 5 faturamento total
def faturamento_total(pedidos):
    soma_faturamento = 0
    for pedido in pedidos:
        if pedido['status'] != "Cancelado":
            fatu = faturamento(pedido) # calcula o faturamento
            soma_faturamento += fatu # acumula os faturamentos dos pedidos
    return soma_faturamento # retorna o faturamento total

# 6 faturamento por categoria
def faturamento_categoria(pedidos):
    categoria = dict() # dict dinâmico
    for pedido in pedidos: # for para rodar na lista
        if pedido['categoria'] not in categoria: # se a categoria não estiver no Dict dinâmico (categoria)
            categoria[pedido['categoria']] = 0 # cria uma key no dict dinâmico com o nome da categoria e seu valor = 0. Exemplo: Eletrônicos: 0
        if pedido['status'] != "Cancelado": # se o status do pedido for diferente de cancelado
            categoria[pedido['categoria']] += faturamento(pedido) # adiciona o valor do faturamento na key dentro do dict dinâmico. Eletônicos: 7000
    return categoria # retorna o dict categoria. {'Eletrônicos': 7240, 'Móveis': 2100}

# 7 Pedido de maior valor
def maior_pedido(pedidos):
    pedidos_validos = [p for p in pedidos if p['status'] != "Cancelado"]
    return max(pedidos_validos, key=lambda pedido: faturamento(pedido))

# 8 Listar por status
def listar_status(status):
    achado = False
    for pedido in pedidos:
        if pedido['status'].lower() == status.lower():
            mostrar_pedido(pedido)
            achado = True
    if not achado:
        print("Nenhum pedido Encontrado!")

# 9 Cancelar Pedido
def cancelar_pedido(pedido):
    if pedido['status'] == "Cancelado":
        print("O pedido já está Cancelado!!!")
    elif pedido['status'] == "Entregue":
        print("O pedido já foi Entregue. Não Pode ser Cancelado!")
    else:
        print(f"{pedido['status']} -> Cancelado")
        pedido['status'] = "Cancelado"
        print("O pedido foi cancelado com sucesso!")

# 10 Cliente que mais gastou
def cliente_maior_gasto(pedidos):
    clientes = dict()
    for pedido in pedidos:
        if pedido['cliente'] not in clientes:
            clientes[pedido['cliente']] = 0
        if pedido['status'] != "Cancelado":
            clientes[pedido['cliente']] += faturamento(pedido)
        # pega os items do dict (key, values), retorna o pedido em forma de tupla: analisando o segundo item da tupla que seria o faturamento
    return max(clientes.items(), key=lambda pedido: pedido[1]) 

pedidos = [
    {"id": 1, "cliente": "João", "produto": "Notebook", "categoria": "Eletrônicos", "quantidade": 2, "preco": 3500.00, "status": "Entregue"},
    {"id": 2, "cliente": "Maria", "produto": "Mouse", "categoria": "Eletrônicos", "quantidade": 3, "preco": 80.00, "status": "Processando"},
    {"id": 3, "cliente": "Carlos", "produto": "Cadeira", "categoria": "Móveis", "quantidade": 1, "preco": 1200.00, "status": "Entregue"},
    {"id": 4, "cliente": "Ana", "produto": "Teclado", "categoria": "Eletrônicos", "quantidade": 2, "preco": 250.00, "status": "Cancelado"},
    {"id": 5, "cliente": "Pedro", "produto": "Mesa", "categoria": "Móveis", "quantidade": 1, "preco": 900.00, "status": "Processando"}
]

while True:
    print("\n==== MENU ====")
    print("1 - Listar pedidos")
    print("2 - Buscar pedido por ID")
    print("3 - Criar pedido")
    print("4 - Alterar status por pedido")
    print("5 - Calcular faturamento total")
    print("6 - Faturamento por categoria")
    print("7 - Pedido de maior valor")
    print("8 - Listar pedidos por status")
    print("9 - Cancelar pedido")
    print("10 - Cliente que mais gastou")
    print("0 - Sair")
    opcao = input("Escolha uma das opções: ")
    print()
    match opcao:
        case "0":
            break
        case "1":
            listar_pedidos()
        case "2":
            print("==== BUSCAR PEDIDO ====")
            id_pedido = int(input("Digite o id do pedido: ").strip())
            pedido = buscar_pedido(id_pedido)
            verificar_busca(pedido)
        case "3":
            print("==== CRIAR PEDIDO ====")
            cliente = input("Digite o nome do cliente: ").strip().capitalize()
            produto = input("Digite o produto: ").strip().capitalize()
            categoria = input("Digite a categoria: ").strip().capitalize()
            while True:
                quantidade = input("Digite a quantidade: ").strip()
               # isdigit() checa se a string tem apenas números de 0 a 9; int(quantidade) > 0 garante que a quantidade seja positiva
                if quantidade.isdigit() and int(quantidade) > 0:
                    quantidade = int(quantidade)
                    break
                else:
                    print("Por Favor! Digite uma quantidade válida!")
            preco = float(input("Digite o preço: ").strip())
            novo_pedido = criar_pedido(cliente, produto, categoria, quantidade, preco)
            print("\nPedido Cadastrado com Sucesso!")
            mostrar_pedido(novo_pedido)
        case "4":
            print("==== ALTERAR STATUS ====")
            id_pedido = int(input("Digite o id do pedido: ").strip())
            pedido = buscar_pedido(id_pedido)
            if pedido:
                print("Pedido Achado!")
                mostrar_pedido(pedido)
                print("1 - Processando")
                print("2 - Enviado")
                print("3 - Entregue")
                print("4 - Cancelado")
                lista_status = [1, 2, 3, 4]
                while True:
                    status = input("Escolha uma das Opções (1-4): ").strip()
                    if status.isdigit() and int(status) in lista_status:
                        status = int(status)
                        break
                    print("ERRO! OPÇÃO INVÁLIDA!")
                alterar_status(pedido, status)
                mostrar_pedido(pedido)
            else:
                print("Pedido Não Encontrado!")

        case "5":
            print("==== Faturamento Total ====")
            print(f"Faturamento Total: R${faturamento_total(pedidos):.2f}")
        case "6":
            print("==== FATURAMENTO POR CATEGORIA ====")
            categorias = faturamento_categoria(pedidos) 
            for k, v in categorias.items():
                print(f"{k}: R${v:.2f}")
        case "7":
            print("==== MAIOR PEDIDO ====")
            maior = maior_pedido(pedidos)
            print(f"Cliente: {maior['cliente']} - Produto: {maior['produto']}: R$ {faturamento(maior):.2f}")
        case "8":
            print("==== LISTA STATUS ====")
            status_disponiveis = {1:"Processando", 2:"Enviado", 3:"Entregue", 4:"Cancelado"}
            while True:
                print("\nSTATUS DISPONÍVEIS: ")
                for v in status_disponiveis.values():
                    print(f"- {v.upper()}")
                status = input("Digite o status: ").strip().capitalize()
                if status in status_disponiveis.values():
                    break
                else:
                    print("\nERRO! Digite um Status Válido!")
            listar_status(status)
        case "9":
            print("=== CANCELAR PEDIDO ====")
            id_pedido = int(input("Digite o id do pedido: ").strip())
            pedido = buscar_pedido(id_pedido)
            verificar_busca(pedido, cancelar_pedido)
        case "10":
            print("==== CLIENTE QUE MAIS GASTOU ====")
            cliente_maior = cliente_maior_gasto(pedidos)
            print(f"Cliente que mais gastou: {cliente_maior[0]}")
            print(f"Total gasto: R$ {cliente_maior[1]:.2f}")
        case _:
            print("Opção Inválida! Escolha uma das Opções!")