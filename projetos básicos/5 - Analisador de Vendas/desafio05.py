def calcular_faturamento(preco, quantidade): 
    # Calcula o valor total de uma venda multiplicando o preço pela quantidade
    return preco * quantidade 


def faturamento_clientes(vendas): 
    # Cria um dicionário que vai guardar o faturamento acumulado de cada cliente
    faturamento_cliente = dict() 

    for cliente in vendas: # vai rodar cada dict da lista de vendas

        # Se o cliente ainda não estiver no dicionário, cria uma chave para ele
        if cliente['cliente'] not in faturamento_cliente: 
            faturamento_cliente[cliente['cliente']] = 0 

        # Calcula o valor da venda e adiciona ao faturamento do cliente correspondente
        # Se o cliente aparecer novamente, o valor será somado ao que ele já possui
        faturamento_cliente[cliente['cliente']] += calcular_faturamento(
            cliente['preco'], 
            cliente['quantidade']
        ) 

    # Retorna o dicionário contendo cada cliente e seu faturamento total
    return faturamento_cliente 
     
     
vendas = [ 
    {"cliente": "João", "produto": "Notebook", "categoria": "Informática", "quantidade": 2, "preco": 3500}, 
    {"cliente": "Maria", "produto": "Mouse", "categoria": "Informática", "quantidade": 5, "preco": 80}, 
    {"cliente": "Carlos", "produto": "Cadeira", "categoria": "Móveis", "quantidade": 3, "preco": 900}, 
    {"cliente": "Ana", "produto": "Teclado", "categoria": "Informática", "quantidade": 4, "preco": 150}, 
    {"cliente": "Pedro", "produto": "Mesa", "categoria": "Móveis", "quantidade": 2, "preco": 1200}, 
    {"cliente": "João", "produto": "Monitor", "categoria": "Informática", "quantidade": 3, "preco": 1800}, 
    {"cliente": "Maria", "produto": "Cadeira", "categoria": "Móveis", "quantidade": 2, "preco": 900}, 
    {"cliente": "Carlos", "produto": "Headset", "categoria": "Informática", "quantidade": 6, "preco": 250}, 
] 
 

# Mantém o programa funcionando até que o usuário escolha a opção 0
while True: 
    print("\n==== ANALISADOR DE VENDAS ====") 
    print("1 - Mostrar todoas as Vendas") 
    print("2 - Faturamento total") 
    print("3 - Maior Venda") 
    print("4 - Menor Venda") 
    print("5 - Faturamento Por Categoria") 
    print("6 - Produto Mais Vendido") 
    print("7 - Faturamento Por Cliente") 
    print("8 - Cliente Que Mais Gastou") 
    print("0 - Sair") 

    # Recebe a opção escolhida pelo usuário como string
    opcao = input("Escolha uma das opções: ") 
 

    # Verifica qual opção foi escolhida pelo usuário
    match opcao: 

        case "0": 
            # Encerra o while True e finaliza o programa
            break 


        case "1": 
            # 1 Vai Mostrar Todas as Vendas 
            print("\n==== TODAS AS VENDAS ====") 

            # Percorre cada dicionário da lista de vendas
            for cliente in vendas: 

                # Mostra o cliente, o produto e o valor total daquela venda
                print(
                    f"{cliente['cliente']}: {cliente['produto']} -> "
                    f"{calcular_faturamento(cliente['preco'], cliente['quantidade'])}"
                ) 


        case "2": 
            # 2 Faturamento Total e Quantidade total vendida 
            print("\n==== FATURAMENTO TOTAL ====") 

            # Acumulador que vai guardar o faturamento de todas as vendas
            faturamento_total = 0 

            # Acumulador que vai guardar a quantidade total de produtos vendidos
            quant_total = 0 

            for cliente in vendas: 

                # vai calcular o faturamento de cada produto
                produto_faturamento = calcular_faturamento(
                    cliente['preco'], 
                    cliente['quantidade']
                ) 

                # vai somando o faturamento de cada produto
                faturamento_total += produto_faturamento 

                # vai somando a quantidade de cada produto
                quant_total += cliente['quantidade'] 

            print(f"Faturamento Total: R${faturamento_total:.2f}") 
            print(f"Quantidade Total de Produtos Vendidos: {quant_total}") 


        case "3":  
            # 3 Venda de Maior Valor 
            print("\n==== VENDA DE MAIOR VALOR ====") 

            # max() percorre a lista de vendas e o lambda define que a comparação
            # será feita pelo valor total de cada venda
            # vai retornar o dict da venda de maior valor
            maior_valor = max(
                vendas, 
                key=lambda cliente: calcular_faturamento(
                    cliente['preco'], 
                    cliente['quantidade']
                )
            ) 

            print(f"Cliente: {maior_valor['cliente']}") 
            print(f"Produto: {maior_valor['produto']}") 

            # Recalcula o faturamento da venda encontrada para exibir seu valor
            print(
                f"Valor da Venda: "
                f"R${calcular_faturamento(maior_valor['preco'], maior_valor['quantidade']):.2f} "
            ) 


        case "4": 
            # 4 Venda de menor Valor 
            print("\n==== VENDA DE MENOR VALOR ====") 

            # min() percorre a lista de vendas e o lambda define que a comparação
            # será feita pelo valor total de cada venda
            # vai retornar o dict da venda de menor valor
            menor_valor = min(
                vendas, 
                key=lambda cliente: calcular_faturamento(
                    cliente['preco'], 
                    cliente['quantidade']
                )
            ) 

            print(f"Cliente: {menor_valor['cliente']}") 
            print(f"Produto: {menor_valor['produto']}") 

            # Recalcula o faturamento da venda encontrada para exibir seu valor
            print(
                f"Valor da Venda: "
                f"R${calcular_faturamento(menor_valor['preco'], menor_valor['quantidade']):.2f} "
            ) 


        # 5 Faturamento por Categoria 
        case "5":  
            print("\n==== FATURAMENTO POR CATEGORIA ====") 

            # dicionário que vai guardar o faturamento acumulado de cada categoria
            faturamento_categoria = dict() 

            # vai rodar cada dict da lista
            for cliente in vendas: 

                # Se a categoria não estiver no dict, cria a chave
                if cliente['categoria'] not in faturamento_categoria: 

                    # Inicializa a chave com o valor 0 para começar o acumulador
                    faturamento_categoria[cliente['categoria']] = 0 
                    
                # Esta linha roda SEMPRE (para categorias novas e já existentes).
                # Se tivesse colocado dentro de um else, não iria somar a primeira venda.
                # Ela acumula o valor calculado na chave correspondente.
                faturamento_categoria[cliente['categoria']] += calcular_faturamento(
                    cliente['preco'], 
                    cliente['quantidade']
                ) 

            # .items() permite percorrer a chave e o valor do dicionário ao mesmo tempo
            for k, v in faturamento_categoria.items(): 
                print(f"{k}: R${v:.2f}") 


        case "6": 
            # 6 Produto mais vendido em quantidade 
            print("\n==== PRODUTO MAIS VENDIDO ====") 

            # vai guardar a quantidade vendida de cada produto
            quantidade_vendida = dict() 

            # vai rodar cada dict da lista
            for venda in vendas: 

                # Se o produto não estiver no dict, cria uma chave para ele
                if venda['produto'] not in quantidade_vendida: 

                    # coloca o produto como chave com seu valor = 0
                    quantidade_vendida[venda['produto']] = 0 

                # adiciona a quantidade vendida do produto ao valor da chave
                # Se o mesmo produto aparecer novamente, a quantidade será acumulada
                quantidade_vendida[venda['produto']] += venda['quantidade'] 

            # .items() transforma o dicionário em pares (produto, quantidade)
            # O lambda usa o segundo elemento da tupla [1] para comparar as quantidades
            # max() retorna a tupla do produto que possui a maior quantidade
            mais_vendido = max(
                quantidade_vendida.items(), 
                key=lambda prod: prod[1]
            ) 

            # [0] acessa o nome do produto e [1] acessa a quantidade vendida
            print(f"{mais_vendido[0]}: {mais_vendido[1]}") 


        case "7": 
            print("\n==== FATURAMENTO POR CLIENTE ====") 

            # Chama a função que calcula quanto cada cliente gastou
            # e guarda o dicionário retornado pela função
            dict_fatura_clientes = faturamento_clientes(vendas) 

            # Percorre as chaves e valores do dicionário
            for k, v in dict_fatura_clientes.items(): 
                print(f"{k}: R${v:.2f}") 


        case "8": 
            # 8 Cliente que mais gastou 
            print("\n==== MELHOR CLIENTE ====") 

            # A função retorna um dicionário com cliente -> faturamento total
            # .items() transforma esse dicionário em pares (cliente, faturamento)
            #
            # 1. faturamento_clientes(vendas).items(): 
            #    Transforma o dicionário em pares (chave, valor)
            #    no formato de tuplas ('Cliente', total).
            #
            # 2. key=lambda cliente: cliente[1]:
            #    Diz ao max() para comparar apenas o SEGUNDO elemento
            #    de cada tupla, que é o valor faturado. e retorna a chave e o valor
            #
            # 3. max(...):
            #    Encontra e retorna a tupla completa do cliente que
            #    teve o maior valor.
            melhor_cliente = max(
                faturamento_clientes(vendas).items(), key=lambda cliente: cliente[1]) 

            # 4. melhor_cliente[0]:
            #    Acessa o primeiro elemento da tupla, que é o nome do cliente.
            #
            # 5. melhor_cliente[1]:
            #    Acessa o segundo elemento da tupla, que é o valor do faturamento.
            #    :.2f formata o valor para mostrar duas casas decimais.
            print(f"{melhor_cliente[0]}: R${melhor_cliente[1]:.2f}") 


        case _: 
            # Caso o usuário digite uma opção que não existe no menu
            print("Opção Inválida! Tente Novamente!") 


# O método .get é uma função nativa dos dicionários no Python.
# Em termos simples: ele serve para buscar/pegar o valor de uma chave.