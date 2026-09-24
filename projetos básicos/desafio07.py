from random import randint

# 1 - listar livros
def listar_livros():
    for livro in livros:
        print(f"Id: {livro['id']}")
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Categoria: {livro['categoria']}")
        print(f"Ano: {livro['ano']}")
        print(f"Disponível: {livro['disponivel']}")
        print("-"*30)

# 2 - Buscar livro
def buscar_livro(id_livro):
    for livro in livros:
        if livro['id'] == id_livro:
            return livro
        
def verificar_busca(livro, funcao=None):
    if livro:
        print("\nLivro encontrado!")
        if funcao: # se tiver alguma função como parâmetro
            funcao(livro) # Executa ações como emprestar ou devolver (se informadas)
        mostrar_livro(livro) # Exibe os dados atualizados do livro
    else:
        print("\nLivro não encontrado!")

def mostrar_livro(livro):
    print("-"*30)
    print(f"Id: {livro['id']}")
    print(f"Título: {livro['titulo']}")
    print(f"Autor: {livro['autor']}")
    print(f"Categoria: {livro['categoria']}")
    print(f"Ano: {livro['ano']}")
    print(f"Disponível: {livro['disponivel']}")
    print("-"*30)
    print()

# 3 - cadastrar livro
def cadastrar_livro(titulo, autor, categoria, ano):
    livro_novo = dict()
    if not livros:
        livro_novo['id'] = 1
    else :
        ids_existentes = [livro['id'] for livro in livros]
        id_novo = randint(1, 100)
        while id_novo in ids_existentes:
            id_novo = randint(1, 100)
        livro_novo['id'] = id_novo
    livro_novo['titulo'] = titulo
    livro_novo['autor'] = autor
    livro_novo['categoria'] = categoria
    livro_novo['ano'] = ano
    livro_novo['disponivel'] = True
    livros.append(livro_novo)
    return livro_novo

# 4 - emprestar livro
def emprestar_livro(livro):
    if livro['disponivel']:
        livro['disponivel'] = False
        print("Livro emprestado com Sucesso!")
    else:
        print("O livro já está emprestado!")

# 5 - devolver livro
def devolver_livro(livro):
    if not livro['disponivel']:
        livro['disponivel'] = True
        print("Livro devolvido com Sucesso!")
    else:
        print('O livro já está disponível')
        
# 6 - livro disponível
def livros_disponiveis():
    for livro in livros:
        if livro['disponivel']:
            print(f"{livro['titulo']}")

# 7  Quantidade de livros por categoria
def quantidade_livro_categoria(livros):
    categorias = dict()
    for livro in livros:
        if livro['categoria'] not in categorias:
            categorias[livro['categoria']] = 0
        categorias[livro['categoria']] += 1
    return categorias

# 8 Livro mais antigo
def livro_antigo(livros):
    mais_antigo = min(livros, key= lambda livro: livro['ano'])
    return mais_antigo

# 9  Livro mais recente
def livro_recente(livros):
    mais_recente = max(livros, key=lambda livro: livro['ano'])
    return mais_recente

# 10 Buscar livros por autor
def buscar_autor(autor):
    livros_autor = list()
    for livro in livros:
        if livro['autor'].lower() == autor.lower(): # para fazer a comparação entre minúsculas, não importando em como o usuário irá digitar o texto
            livros_autor.append(livro['titulo'])
    return livros_autor

livros = [
    {
        "id": 1,
        "titulo": "Dom Casmurro",
        "autor": "Machado de Assis",
        "categoria": "Romance",
        "ano": 1899,
        "disponivel": True
    },
    {
        "id": 2,
        "titulo": "O Hobbit",
        "autor": "J.R.R. Tolkien",
        "categoria": "Fantasia",
        "ano": 1937,
        "disponivel": True
    },
    {
        "id": 3,
        "titulo": "1984",
        "autor": "George Orwell",
        "categoria": "Ficção",
        "ano": 1949,
        "disponivel": False
    },
    {
        "id": 4,
        "titulo": "O Pequeno Príncipe",
        "autor": "Antoine de Saint-Exupéry",
        "categoria": "Infantil",
        "ano": 1943,
        "disponivel": True
    },
    {
        "id": 5,
        "titulo": "Harry Potter e a Pedra Filosofal",
        "autor": "J.K. Rowling",
        "categoria": "Fantasia",
        "ano": 1997,
        "disponivel": True
    },
    {
    "id": 6,
    "titulo": "O Alienado",
    "autor": "Machado de Assis",
    "categoria": "Ficção",
    "ano": 1885,
    "disponivel": False
    }
]

while True:
    print("==== SISTEMA DE BIBLIOTECA ====")
    print("1 - Listar livros")
    print("2 - Buscar livro")
    print("3 - Cadastrar livro")
    print("4 - Emprestar livro")
    print("5 - Devolver livro")
    print("6 - Listar livros disponíveis")
    print("7 - Quantidade de livros por categoria")
    print("8 - Livro mais antigo")
    print("9 - Livro mais recente")
    print("10 - Buscar livros por autor")
    print("0 - Sair")

    opcao = input("Escolha uma das opções: ")
    match opcao:
        case "0":
            break
        case "1":
            listar_livros()
        case "2":
            print("\n==== BUSCAR LIVRO ====")
            id_buscar = int(input("Digite o id do livro que procura: "))
            livro = buscar_livro(id_buscar)
            verificar_busca(livro)
        case "3":
            print("\n==== CADASTRO LIVRO ====")
            titulo = input("Digite o título: ").strip().title()
            autor = input("Digite o autor: ").strip()
            categoria = input("Digite a categoria: ").strip().capitalize()
            ano = int(input("Digite o ano: ").strip())
            novo_livro = cadastrar_livro(titulo, autor, categoria, ano)
            print("\nLivro Cadastrado com Sucesso!")
            mostrar_livro(novo_livro)
        case "4":
            id_buscar = int(input("Digite o id do livro que procura: "))
            livro = buscar_livro(id_buscar)
            verificar_busca(livro, emprestar_livro)
        case "5":
            id_buscar = int(input("Digite o id do livro que procura: "))
            livro = buscar_livro(id_buscar)
            verificar_busca(livro, devolver_livro)
        case "6":
            print("\n==== LIVROS DISPONÍVEIS ====")
            livros_disponiveis()
            print()
        case "7":
            print("\n==== QUANTIDADE DE LIVROS POR CATEGORIA ====")
            categorias = quantidade_livro_categoria(livros)
            for k, v in categorias.items():
                print(f"{k}: {v}")
            print()
        case "8":
            print("\n==== LIVRO MAIS ANTIGO ====")
            livro_mais_antigo = livro_antigo(livros)
            print(livro_mais_antigo['titulo'])
            print(livro_mais_antigo['ano'])
            print()
        case "9":
            print("\n==== LIVRO MAIS RECENTE ====")
            livro_mais_recente = livro_recente(livros)
            print(livro_mais_recente['titulo'])
            print(livro_mais_recente['ano'])
            print()
        case "10":
            print("\n==== BUSCA DE LIVRO POR AUTOR ====")
            autor_buscar = input("Digite o nome do autor: ").strip()
            autor_livro = buscar_autor(autor_buscar)
            if autor_livro:
                print("Livro Encontrado!")
                print("--Livros: ")
                for titulo in autor_livro:
                    print(f"{titulo}")
            else:
                print("Livro do Autor não encontrado!")
        case _:
            print("\nOPÇÃO INVÁLIDA! TENTE NOVAMENTE\n")
