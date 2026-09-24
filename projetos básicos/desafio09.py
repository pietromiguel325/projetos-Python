from random import randint

# 1 
def listar_produtos():
    for produto in produtos:
        print(f"ID: {produto['id']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: R${produto['preco']:.2f}")
        print(f"Estoque: {produto['estoque']}")
        print("-"*30)

# 2
def buscar_produto(id):
    for produto in produtos:
        if produto['id'] == id:
            return produto

def verificar_buscar(produto, funcao=None):
    if produto:
        print("Produto Encontrado!")
        if funcao: # usa no 4 e 5
            funcao(produto)
        mostrar_produto(produto)
    else:
        print("Produto Não Encontrado!")

def mostrar_produto(produto):
    print("-"*30)
    print(f"ID: {produto['id']}")
    print(f"Nome: {produto['nome']}")
    print(f"Categoria: {produto['categoria']}")
    print(f"Preço: R${produto['preco']:.2f}")
    print(f"Estoque: {produto['estoque']}")
    print("-"*30)

# 3
def cadastrar_produto(nome, categoria, preco, estoque):
    produto_novo = dict()
    if produtos:
        ids_cadastrados = [produto['id'] for produto in produtos]
        id_novo = randint(1, 100)
        while id_novo in ids_cadastrados:
            id_novo = randint(1, 100)
    else:
        id_novo = 1
    produto_novo['id'] = id_novo
    produto_novo['nome'] = nome 
    produto_novo['categoria'] = categoria
    produto_novo['preco'] = preco
    produto_novo['estoque'] = estoque
    produtos.append(produto_novo)
    print("Produto Cadastrado com Sucesso!")
    return produto_novo  

def adicionar_estoque(produto):
    entrada = int(input("Digite a quantidade de entrada: "))
    print("-"*30)
    print(f'Estoque atual: {produto['estoque']}')
    print(f"Entrada: +{entrada}")
    print(f"Novo Estoque: {entrada + produto['estoque']}")
    produto['estoque'] += entrada

def saida_estoque(produto):
    saida = int(input("Digite a quantidade de saída: "))
    print("-"*30)
    if saida > produto['estoque']:
        print("Erro! Estoque Insuficiente")
    else:
        print(f"Estoque atual: {produto['estoque']}")
        print(f"Saída: -{saida}")
        print(f"Novo estoque: {produto['estoque'] - saida}")
        produto['estoque'] -= saida

def verifica_id(entrada):
    while True:
        if entrada.isdigit() and int(entrada) > 0 and int(entrada) <= 100:
            entrada = int(entrada) 
            break #
        else:
            entrada = input("Por Favor! Digite o id do produto novamente (0-100): ") 
    return entrada 

def estoque_baixo(produtos):
    for produto in produtos:
        if produto['estoque'] <= 5:
            mostrar_produto(produto)

def calcular_fatura(produto):
    return produto['preco'] * produto['estoque']

def valor_total_estoque(produtos):
    soma = 0
    for produto in produtos:
        faturamento = calcular_fatura(produto)
        soma += faturamento
    return soma

def maior_quantidade():
    return max(produtos, key=lambda produto: produto['estoque'])

def produto_mais_caro():
    return max(produtos, key=lambda produto: produto['preco'])

def calcular_valor_categoria():
    categorias = dict()
    for produto in produtos:
        if produto['categoria'] not in categorias:
            categorias[produto['categoria']] = 0
        categorias[produto['categoria']] += calcular_fatura(produto)
    return categorias

produtos = [
    {"id": 1,"nome": "Notebook","categoria": "Eletrônicos","preco": 3500.00,"estoque": 10},
    {"id": 2, "nome": "Mouse", "categoria": "Eletrônicos", "preco": 120.00, "estoque": 7},
    {"id": 3,"nome": "Mesa","categoria": "Móveis","preco": 675.00,"estoque": 3},
    {"id": 4, "nome": "Boné", "categoria": "Vestuário", "preco": 75.00, "estoque": 13},
    {"id": 5,"nome": "Cadeira","categoria": "Móveis","preco": 45.00,"estoque": 5},
    {"id": 6, "nome": "Camisa", "categoria": "Vestuário", "preco": 89.00, "estoque": 8},
]

while True:
    print("\n==== SISTEMA DE ESTOQUE ====")
    print("1 - Listar Produtos")
    print("2 - Buscar Produto Por ID")
    print("3 - Cadastrar Produto")
    print("4 - Entrada de Estoque")
    print("5 - Saída de Estoque")
    print("6 - Produtos com Estoque Baixo")
    print("7 - Valor Total do Estoque")
    print("8 - Produto com Maior Estoque")
    print("9 - Produto mais Caro")
    print("10 - Valor do Estoque por Categoria")
    print("0 - Sair")
    opcao = input("Escolha uma das opções: ")
    print()
    match opcao:
        case "0":
            break
        case "1":
            print("--- LISTA DE PRODUTOS ---")
            listar_produtos()
        case "2":
            print("--- BUSCAR PRODUTO ---")
            id_buscar = input("Digite o id do produto (0-100): ")
            id_verificado = verifica_id(id_buscar)
            produto = buscar_produto(id_verificado)
            verificar_buscar(produto)
        case "3":
            print("--- CADASTRAR PRODUTO ---")
            nome = input("Digite o nome do produto: ").strip().capitalize()
            categoria = input("Digite a categoria do produto: ").strip().capitalize()
            preco = float(input("Digite o preço do produto: "))
            estoque = input("Digite a quantidade: ")
            while True:
                if estoque.isdigit() and int(estoque) > 0:
                    estoque = int(estoque)
                    break
                else:
                    estoque = input("Por Favor! Digite uma quantidade válida: ")
            novo_produto = cadastrar_produto(nome, categoria, preco, estoque)
            mostrar_produto(novo_produto)
        case "4":
            print("--- ENTRADA ESTOQUE ---")
            id_buscar = input("Digite o id do produto (0-100): ")
            id_verificado = verifica_id(id_buscar)
            produto = buscar_produto(id_verificado)
            verificar_buscar(produto, adicionar_estoque)
        case "5":
            id_buscar = input("Digite o id do produto (0-100): ")
            id_verificado = verifica_id(id_buscar)
            produto = buscar_produto(id_verificado)
            verificar_buscar(produto, saida_estoque)
        case "6":
            print("--- PRODUTOS COM ESTOQUE BAIXO ---")
            estoque_baixo(produtos)
        case "7":
            print("--- VALOR TOTAL DO ESTOQUE --")
            faturamento_total = valor_total_estoque(produtos)
            print(f"Valor Total do estoque: R${faturamento_total:.2f}")
        case "8":
            print("--- PRODUTO COM MAIOR ESTOQUE ---")
            maior = maior_quantidade()
            print(f"{maior['nome']}: {maior['estoque']}")
        case "9":
            print("--- PRODUTO MAIS CARO ---")
            caro = produto_mais_caro()
            print(f"{caro['nome']}: R${caro['preco']:.2f}")
        case "10":
            print("--- VALOR DO ESTOQUE POR CATEGORIA ---")
            categorias = calcular_valor_categoria()
            for k, v in categorias.items():
                print(f"{k}: R${v:.2f}")
        case _:
            print("ERRO! POR FAVOR, SELECIONE UMA DAS OPÇÕES")