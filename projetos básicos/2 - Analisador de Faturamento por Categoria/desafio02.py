def calcular_faturamento(qtd, preco):
    return qtd*preco

vendas = [
    {"produto": "Notebook", "categoria": "Informática", "quantidade": 3, "preco": 3500},
    {"produto": "Mouse", "categoria": "Informática", "quantidade": 15, "preco": 80},
    {"produto": "Teclado", "categoria": "Informática", "quantidade": 8, "preco": 150},
    {"produto": "Cadeira", "categoria": "Móveis", "quantidade": 5, "preco": 900},
    {"produto": "Mesa", "categoria": "Móveis", "quantidade": 2, "preco": 1200},
    {"produto": "Headset", "categoria": "Informática", "quantidade": 10, "preco": 250},
]
faturamento_total = 0
qtd_total = 0
faturamento_categoria = dict()
maior = 0
maior_nome = ""
print("==== PEDIDOS(VENDAS) ====")
for produto in vendas:

    valor_produto = calcular_faturamento(produto['quantidade'], produto['preco']) # variável que armazena faturamento do produto
    faturamento_total += valor_produto  # acumulador que vai somando o faturamento total

    # condicional para ver o produto com maior faturamento
    if valor_produto > maior: 
        maior = valor_produto #guarda 
        maior_nome = produto['produto']

    categoria = produto['categoria']
    if categoria not in faturamento_categoria: # Se a categoria não estiver no dict 
        faturamento_categoria[categoria] = 0 # cria a chave da categoria com o valor 0

    faturamento_categoria[categoria] += valor_produto # pega o valor_produto e soma dentro da chave(categoria correspondente)

    qtd_produto = produto['quantidade'] # variável que guarda a quantidade de produto correspondente
    qtd_total += qtd_produto # acumulador para ir somando a quantidade de produtos

 
    print(f"Produto: {produto['produto']}")
    print(f"categoria: {produto['categoria']}")
    print(f"Valor Produto: R${valor_produto:.2f}")
    print()

print(f"Quantidade total: {qtd_total}")
print(f"Faturamento total: R${faturamento_total:.2f}")

print(f"Produto com maior faturamento: {maior_nome} no valor de R${maior:.2f}")
print("==== FATURAMENTO CATEGORIA ====")
for k, v in faturamento_categoria.items():
    print(f"{k}: R${v:.2f}")


# Outra forma de determinar o maior pedido -> fica fora do loop
# maior_pedido = max(vendas,key=lambda produto: calcular_faturamento(produto['quantidade'], produto['preco']))

# ==============================================================================
# ANOTAÇÕES: QUANDO USAR IF TERNÁRIO VS. LAMBDA / DEF
# ==============================================================================
#
# 📌 REGRA DE OURO:
# - Se o valor JÁ FOI CALCULADO no seu código: Use 'IF / ELSE TERNÁRIO'.
# - Se o Python precisa APRENDER A CALCULAR item por item: Use 'LAMBDA' ou 'DEF'.
#
# ------------------------------------------------------------------------------
#
# 🛠️ CASO 1: A conta já está pronta numa variável (Use IF Ternário)
#
#    Como o valor já existe na memória, você só precisa testar a condição.
#    Não faz sentido criar uma função para reavaliar algo já calculado.
#
#    Exemplo:
#    valor_produto = calcular_faturamento(p['qtd'], p['preco'])
#    valor_info = valor_produto if p['categoria'] == "Informática" else 0
#
# ------------------------------------------------------------------------------
#
# 🛠️ CASO 2: Você precisa passar uma "Regra de Cálculo" para o Python (Use Lambda/Def)
#
#    Funções como max(), sorted() e filter() precisam receber uma instrução/fórmula
#    para aplicarem sozinhas em cada elemento da lista.
#
#    Exemplo (Lambda criada na hora):
#    maior = max(vendas, key=lambda p: calcular(p['qtd'], p['preco']) if p['categoria'] == "Informática" else 0)
#
#    Exemplo (Lambda em variável separada):
#    regra_info = lambda p: calcular(p['qtd'], p['preco']) if p['categoria'] == "Informática" else 0
#    maior = max(vendas, key=regra_info)
#
#    Exemplo (Função def normal - mais legível):
#    def regra_info(p):
#        if p['categoria'] == "Informática":
#            return calcular(p['qtd'], p['preco'])
#        return 0
#
#    maior = max(vendas, key=regra_info)
#
# ==============================================================================
# RESUMO EM 1 LINHA:
# "If ternário checa um valor que já existe; Lambda/Def cria uma regra para calcular depois."
# ==============================================================================