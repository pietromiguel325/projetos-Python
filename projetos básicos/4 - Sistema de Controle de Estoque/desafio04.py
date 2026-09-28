from random import randint

# Função responsável por listar todos os produtos cadastrados
def listar_produtos():
    for produto in produtos:
        print(f"Id: {produto['id']}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Preço: {produto['preco']}")
        print(f"Estoque: {produto['estoque']}")
        print()

# def mostrar_produto(id_produto): # neste ele procura o id na lista, percorre a lista até achar o id
#     for produto in produtos:
#         if produto['id'] == id_produto:
#             print(f"Nome: {produto['nome']}")
#             print(f"Categoria: {produto['categoria']}")
#             print(f"Preço: {produto['preco']}")
#             print(f"Estoque: {produto['estoque']}")

def mostrar_produto(produto): # neste ele pede para colocar o dict do produto, não precisando procurar na lista
    print(f"Nome: {produto['nome']}")
    print(f"Categoria: {produto['categoria']}")
    print(f"Preço: {produto['preco']}")
    print(f"Estoque: {produto['estoque']}")

# Função responsável por procurar um produto pelo ID
def buscar_produto(id_produto):
    for produto in produtos:
        # Compara o ID informado pelo usuário com o ID de cada produto
        if produto['id'] == id_produto:
            return produto # vai retornar o dict do produto

# Função responsável por adicionar uma quantidade ao estoque do produto
def entrada_estoque(produto, quantidade_estoque):
    produto['estoque'] += quantidade_estoque
    return produto['estoque'] # número do novo estoque

# Função responsável por verificar se o produto foi encontrado
def verificar_busca(produto):
    if produto:
        print("\nProduto Encontrado com Sucesso!")
        mostrar_produto(produto)
    else:
        print("Produto Não Encontrado!")

# Função responsável por verificar quais produtos estão com estoque baixo
def estoque_baixo(produtos): # vai receber a lista produtos
    encontrou = False # 1. Ponto de partida: assumimos que NINGUÉM tem estoque baixo

    for produto in produtos: # vai rodar cada produto da lista
        if produto['estoque'] < 5: # cada produto que tiver o estoque < 5
            print("Produto com Estoque Baixo: ")
            print(f"{produto['nome']} -> estoque {produto['estoque']}") # vai imprimir o nome do produto, a quantidade que tem no estoque
            encontrou = True # 2. Se o código entrar AQUI, mudamos para True!

    if not encontrou: # 3. O 'not False' vira True -> Imprime o aviso!
        print("Nenhum produto está com o estoque baixo!")

# Função responsável por calcular o valor total dos produtos que estão no estoque
def calcular_valor_estoque(produtos): # vai receber a lista de produtos
    valor_estoque_total = 0 # acumulador que vai armazenar o valor total do estoque

    for produto in produtos:
        preco = produto['preco'] # pega o preço do produto
        estoque = produto['estoque'] # pega a quantidade disponível no estoque

        valor_produto = preco * estoque # calcula quanto vale o estoque daquele produto
        valor_estoque_total += valor_produto # acumula o valor de cada produto

        print(f"{produto['nome']} -> {preco} X {estoque} = R${valor_produto:.2f}")

    print(f"Valor Total do Estoque: R${valor_estoque_total:.2f}")


# Lista contendo os produtos cadastrados inicialmente
produtos = [
    {"id": 1, "nome": "Notebook", "categoria": "Informática", "preco": 3500, "estoque": 8},
    {"id": 2, "nome": "Mouse", "categoria": "Informática", "preco": 80, "estoque": 25},
    {"id": 3, "nome": "Teclado", "categoria": "Informática", "preco": 150, "estoque": 12},
    {"id": 4, "nome": "Cadeira", "categoria": "Móveis", "preco": 900, "estoque": 5},
    {"id": 5, "nome": "Mesa", "categoria": "Móveis", "preco": 1200, "estoque": 3},
]

# Mantém o sistema funcionando até que o usuário escolha a opção 0
while True:
    print("\n==== SISTEMA DE ESTOQUE ====")
    print("1 - Listar produtos")
    print("2 - Buscar produto")
    print("3 - Cadastrar produtos")
    print("4 - Entrada de estoque")
    print("5 - Saída de estoque")
    print("6 - Produtos com estoque baixo")
    print("7 - Valor total do estoque")
    print("0 - Sair")

    # Converte o valor digitado pelo usuário de string para inteiro
    opcao = int(input("\nSelecione uma das opções: "))

    # Verifica qual opção foi escolhida pelo usuário
    match opcao:

        case 0:
            # Encerra o while True e, consequentemente, o programa
            break

        case 1:
            # Chama a função responsável por listar todos os produtos
            listar_produtos()

        case 2:
            # Solicita o ID do produto que o usuário deseja procurar
            buscar_id = int(input("\nDigite o id do Produto: "))

            # vai percorrer a lista procurando o id do produto
            produto_procurado = buscar_produto(buscar_id)

            # Verifica se o produto foi encontrado e mostra seus dados
            verificar_busca(produto_procurado)

        case 3:
            # Cria um novo dicionário que armazenará os dados do produto
            novo_produto = dict()

            # Verifica se a lista de produtos está vazia
            if not produtos: # se a lista de produtos estiver vazia
                novo_produto['id'] = 1 # o primeiro id vai ser 1

            else:
                # Cria uma lista contendo apenas os IDs dos produtos existentes
                ids_existentes = [p['id'] for p in produtos] # nova lista que contém os ids que existem

                # Gera um ID aleatório entre 1 e 100
                id_novo = randint(1, 100) # vai gerar o id novo

                # Continua gerando um novo ID enquanto o número já existir
                while id_novo in ids_existentes: # enquanto o id_novo for igual aos existentes
                    id_novo = randint(1, 100) # vai ficar gerando um novo_id

                # Guarda o ID que não está sendo utilizado no novo produto
                novo_produto['id'] = id_novo

            # Solicita os dados do novo produto
            novo_produto['nome'] = input("Digite o nome: ")
            novo_produto['categoria'] = input("Digite a categoria: ")
            novo_produto['preco'] = float(input("Digite o preço: "))
            novo_produto['estoque'] = int(input("Digite a quantidade: "))

            # adiciona o dicionário na lista
            produtos.append(novo_produto)

            print("Produto Cadastrado com Sucesso!")

        case 4:
            # Solicita o ID do produto que receberá a entrada de estoque
            buscar_id = int(input("\nDigite o id do Produto: "))

            # Procura o produto pelo ID informado
            produto_procurado = buscar_produto(buscar_id)

            if produto_procurado:
                print("Produto Encontrado com Sucesso!")
                print(f"Nome: {produto_procurado['nome']}")
                print(f"Estoque: {produto_procurado['estoque']}")

                # Solicita a quantidade que será adicionada ao estoque
                quant_entrada = int(input("\nDigite a Quantidade que deseja adicionar: "))

                # Adiciona a quantidade informada ao estoque do produto
                entrada_estoque(produto_procurado, quant_entrada)

                print("Quantidade Adicionada com Sucesso!")

            else:
                print("Produto Não Encontrado!")

        case 5:
            # Solicita o ID do produto que terá uma saída de estoque
            buscar_id = int(input("\nDigite o id do Produto: "))

            # Procura o produto pelo ID informado
            produto_procurado = buscar_produto(buscar_id)

            if produto_procurado:
                print(f"Estoque Atual: {produto_procurado['estoque']}")

                # Solicita a quantidade que será retirada do estoque
                quant_saida = int(input("Saída Solicitada: "))

                # Verifica se existe quantidade suficiente no estoque
                if quant_saida <= produto_procurado['estoque']:

                    # Diminui a quantidade solicitada do estoque
                    produto_procurado['estoque'] -= quant_saida

                    print("Estoque diminuído com Sucesso!")

                else:
                    print("\nEstoque Insuficiente!")
                    print(f"Estoque atual: {produto_procurado['estoque']}")

            else:
                print("Produto Não Encontrado!")

        case 6:
            # Chama a função que verifica quais produtos possuem estoque abaixo de 5 unidades
            estoque_baixo(produtos)

        case 7:
            # Calcula e exibe o valor total dos produtos disponíveis no estoque
            calcular_valor_estoque(produtos)
        case _:
                print("Operação Inválida! Tente Novamente")