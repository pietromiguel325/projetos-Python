# 1. Função customizada para calcular o valor total de um pedido
def valor_total(quantidade, preco):
    return quantidade * preco

# Lista de pedidos (lista de dicionários)
pedidos = [
    {"cliente": "João", "produto": "Mouse", "quantidade": 2, "preco": 80},
    {"cliente": "Maria", "produto": "Teclado", "quantidade": 1, "preco": 150},
    {"cliente": "Carlos", "produto": "Monitor", "quantidade": 2, "preco": 900},
    {"cliente": "Ana", "produto": "Headset", "quantidade": 3, "preco": 250},
]

# 2. Variável acumuladora para o faturamento geral
faturamento_total = 0

# 3. Busca o maior pedido UMA ÚNICA VEZ (fora do loop)
# O max() analisa a lista inteira e guarda apenas o dicionário do pedido de maior valor total
maior_pedido = max(pedidos, key=lambda dic: dic['quantidade'] * dic['preco'])

print("===== PEDIDOS =====")

# 4. Loop para percorrer cada dicionário da lista de pedidos
for dic in pedidos:
    # Calcula o total do pedido atual usando a função
    total_item = valor_total(dic['quantidade'], dic['preco'])
    
    # Exibe as informações do pedido (usando aspas simples nas chaves dentro da f-string)
    print(f"Cliente: {dic['cliente']}")
    print(f"Produto: {dic['produto']}")
    print(f"Quantidade: {dic['quantidade']}")
    print(f"Valor Total: R${total_item:.2f}")
    
    # Soma o valor do pedido ao faturamento acumulado da loja
    faturamento_total += total_item
    print()  # Imprime uma linha em branco entre cada pedido

# 5. Exibe os resumos finais
print(f"Faturamento Total: R${faturamento_total:.2f}\n")

print("==== Maior Pedido ====")
# maior pedido guardou o dicionário do cliente que teve o maior valor do pedido
print(f"Cliente: {maior_pedido['cliente']}")
print(f"Produto: {maior_pedido['produto']}")
# Recalcula o total do maior pedido para exibir
total_maior = valor_total(maior_pedido['quantidade'], maior_pedido['preco'])
print(f"Valor: R${total_maior:.2f}")

# ==============================================================================
# GUIA DEFINITIVO: LAMBDA, KEY E MAX()
# ==============================================================================
#
# 1. A ESTRUTURA DA LAMBDA:
#    lambda ENTRADA : O_QUE_FAZER_COM_A_ENTRADA (A CONTA)
#
#    lambda dic : dic['quantidade'] * dic['preco']
#           |     |________________________________|
#       (ENTRADA)   (A lambda calcula e entrega esse valor ao max)
#
# ------------------------------------------------------------------------------
#
# 2. O QUE É O 'key'?
#    É a REGRA DE COMPARAÇÃO enviada ao max().
#    Como o max() não sabe comparar dicionários inteiros diretamente,
#    o 'key' usa a lambda para extrair um valor numérico de cada um deles.
#
# ------------------------------------------------------------------------------
#
# 3. COMO FUNCIONA NA PRÁTICA (A LÓGICA DO PAPELZINHO 📝):
#
# Instrução:
# maior = max(pedidos, key=lambda dic: dic['quantidade'] * dic['preco'])
#
#  • O max() pega o Dicionário do João (inteiro).
#    Pergunta pra lambda: "Quanto vale esse dicionário?"
#    A lambda responde: "Vale 160".
#    O max() anota no papelzinho: [ João = 160 ]
#
#  • O max() pega o Dicionário da Maria (inteiro).
#    Pergunta pra lambda: "Quanto vale esse dicionário?"
#    A lambda responde: "Vale 150".
#    O max() anota no papelzinho: [ Maria = 150 ]
#
#  • O max() pega o Dicionário do Carlos (inteiro).
#    Pergunta pra lambda: "Quanto vale esse dicionário?"
#    A lambda responde: "Vale 1800".
#    O max() anota no papelzinho: [ Carlos = 1800 ]
#
#  • O max() pega o Dicionário da Ana (inteiro).
#    Pergunta pra lambda: "Quanto vale esse dicionário?"
#    A lambda responde: "Vale 750".
#    O max() anota no papelzinho: [ Ana = 750 ]
#
# ------------------------------------------------------------------------------
#
# 4. CONCLUSÃO E RETORNO:
#
#  - O max() compara todas as anotações: [160, 150, 1800, 750].
#  - Vê que 1800 foi a maior nota de todas (a do Carlos).
#  - O max() RASGA os papelzinhos com os números e TE ENTREGA O DICIONÁRIO DO CARLOS!
#
# RESULTADO SALVO NA VARIÁVEL 'maior':
# {"cliente": "Carlos", "produto": "Monitor", "quantidade": 2, "preco": 900}
# ==============================================================================