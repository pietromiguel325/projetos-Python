from random import randint 
 
# 1 
def listar_chamados(): 
    for chamado in chamados:
        # Vai percorrer cada dict da lista de chamados
        print(f"ID: {chamado['id']}") 
        print(f"Cliente: {chamado['cliente'].capitalize()}") 
        print(f"Categoria: {chamado['categoria'].capitalize()}") 
        print(f"Prioridade: {chamado['prioridade'].capitalize()}") 
        print(f"Status: {chamado['status'].capitalize()}") 
        print(f"Descrição: {chamado['descricao'].capitalize()}") 
        print() 
 
# 2 
def buscar_chamado(id_chamado): 
    for chamado in chamados:
        # Vai percorrer cada dict da lista procurando pelo ID informado
        if chamado['id'] == id_chamado:
            return chamado # coloquei pra retornar o dict, pois vou precisar usar em outras funções 
 
# verifica se o chamado_procurado tem algo dentro, se achou algum chamado ou não 
def verificar_buscar(chamado): # precisa do verificar_buscar, pois se não tiver ele dá erro no mostrar_chamado se não achar o id
    if chamado: # se o dict chamado estiver com algo dentro 
        print("\nChamado Encontrado com Sucesso!") 
        mostrar_chamado(chamado) 
    else: # se não tiver nada dentro 
        print("Chamado Não Encontrado!") 
         
def mostrar_chamado(chamado): # recebe o dict chamado no parâmetro 
    # Mostra as informações do chamado recebido
    print(f"Cliente: {chamado['cliente']}") 
    print(f"Categoria: {chamado['categoria']}") 
    print(f"Prioridade: {chamado['prioridade']}") 
    print(f"Status: {chamado['status']}") 
    print(f"Descrição: {chamado['descricao']}") 
    print() 
 
# 3 
def novo_chamado(cliente, categoria, prioridade, descricao): 
    novo_chamado = dict()
    
    # vai criar uma lista com os ids_existentes 
    ids_existentes = [chamado['id'] for chamado in chamados]
    
    id_novo = randint(1, 100)
    
    # Enquanto o id novo estiver na lista dos ids_existentes
    while id_novo in ids_existentes:
        id_novo = randint(1, 100) # Vai ficar gerando o id até ser diferente 
 
    novo_chamado['id'] = id_novo
    novo_chamado['cliente'] = cliente 
    novo_chamado['categoria'] = categoria 
    novo_chamado['prioridade'] = prioridade 
    
    novo_chamado['status'] = "Aberto" # sempre quando abrir um novo chamado, o status vai ser configurado como aberto 
    
    novo_chamado['descricao'] = descricao 
    
    # Adiciona o novo chamado na lista
    chamados.append(novo_chamado)
    
    return novo_chamado 
 
# 4 
def alterar_status(status, chamado): 
    # Verifica qual opção de status foi escolhida
    match status: 
        case "1": 
            if chamado['status'] == "Aberto": 
                print("Erro Status! Já está Aberto") 
            else: 
                chamado['status'] = "Aberto" 
                print("Status Alterado com Sucesso!") 
        case "2": 
            if chamado['status'] == "Em andamento": 
                print("Erro Status! Em Andamento") 
            else:  
                chamado['status'] = "Em andamento" 
                print("Status Alterado com Sucesso!") 
        case "3": 
            if chamado['status'] == "Resolvido": 
                print("Erro Status! Já está Resolvido") 
            else:  
                chamado['status'] = "Resolvido" 
                print("Status Alterado com Sucesso!") 
        case _: 
            print("Erro! Selecione uma das Opções!") 
 
# 5 
def listar_prioridade(prioridade): 
    for chamado in chamados:
        # Vai percorrer os chamados procurando pela prioridade informada
        if chamado['prioridade'] == prioridade: 
            print(f"Id: {chamado['id']}") 
            mostrar_chamado(chamado) 
 
# 6 
def listar_status(status): 
    for chamado in chamados:
        # Vai percorrer os chamados procurando pelo status informado
        if chamado['status'] == status: 
            print(f"Id: {chamado['id']}") 
            mostrar_chamado(chamado) 
 
# 7 
def contagem_por_categoria(chamados): 
    quantidade_categoria = {}
    
    for chamado in chamados:
        # Se a categoria ainda não estiver no dict, cria a chave com valor 0
        if chamado['categoria'] not in quantidade_categoria: 
            quantidade_categoria[chamado['categoria']] = 0
        
        # Adiciona 1 para cada chamado encontrado naquela categoria
        quantidade_categoria[chamado['categoria']] += 1
    
    return quantidade_categoria 
 
# 8 
def maior_prioridade(chamados): 
    # Dicionário de pesos (de-para): associa o texto da prioridade a um valor numérico 
    # Isso permite comparar as prioridades numericamente (1 < 2 < 3) em vez de alfabeticamente 
    prioridade = { 
        "Baixa": 1, 
        "Média": 2, 
        "Alta": 3 
    } 
     
    # O max() percorre a lista de chamados. 
    # A 'key' recebe uma função lambda que, para cada chamado, busca a prioridade do chamado no dicionário 'prioridade'. 
    # Exemplo: se o chamado tiver prioridade "Alta", prioridade["Alta"] retorna 3. 
    # O max() compara esses números (1, 2 e 3) e seleciona o dicionário do chamado com o maior valor. 
    maior_prioridade = max(chamados, key=lambda chamada: prioridade[chamada['prioridade']]) 
     
    # Retorna o dicionário completo do chamado que teve o maior peso de prioridade 
    return maior_prioridade 
 
# 9 
def encerrar_chamado(resolvido, chamado): 
    # Se o usuário confirmar que o chamado está resolvido
    if resolvido == 's': 
        if chamado['status'] == 'Resolvido': # s + já resolvido → já está resolvido
            print("O chamado já está resolvido!") 
        else: # s + não resolvido      → resolve
            chamado['status'] = "Resolvido" 
            print("Chamado encerrado com sucesso!") 
    else: # n  → não encerra
        # Se o usuário responder "n", não altera o status do chamado
        print("O chamado não foi encerrado.") 
 
chamados = [ 
    { 
        "id": 1, 
        "cliente": "João", 
        "categoria": "Sistema", 
        "prioridade": "Alta", 
        "status": "Aberto", 
        "descricao": "Erro ao fazer login" 
    }, 
    { 
        "id": 2, 
        "cliente": "Maria", 
        "categoria": "Financeiro", 
        "prioridade": "Média", 
        "status": "Em andamento", 
        "descricao": "Problema na emissão da nota" 
    }, 
    { 
        "id": 3, 
        "cliente": "Carlos", 
        "categoria": "Sistema", 
        "prioridade": "Baixa", 
        "status": "Resolvido", 
        "descricao": "Dúvida sobre o sistema" 
    }, 
    { 
        "id": 4, 
        "cliente": "Ana", 
        "categoria": "Acesso", 
        "prioridade": "Alta", 
        "status": "Aberto", 
        "descricao": "Senha não funciona" 
    }, 
    { 
        "id": 5, 
        "cliente": "Pedro", 
        "categoria": "Financeiro", 
        "prioridade": "Alta", 
        "status": "Aberto", 
        "descricao": "Cobrança duplicada" 
    } 
] 
 
 
while True:  
    print("\n==== SISTEMA DE SUPORTE ====") 
    print("1 - Listar chamados") 
    print("2 - Buscar chamado") 
    print("3 - Abrir chamado") 
    print("4 - Alterar status") 
    print("5 - Listar chamados por prioridade") 
    print("6 - Listar chamados por status") 
    print("7 - Quantidade de chamados por categoria") 
    print("8 - Chamado de maior prioridade") 
    print("9 - Encerrar chamado") 
    print("0 - Sair") 
    
    opcao = input("Escolha uma das opções: ")
    
    match opcao: 
        case "0": 
            break 
            
        case "1": 
            print("\n==== TODOS OS CHAMADOS ====") 
            listar_chamados() 
            
        case "2": 
            print("\n==== CHAMADO ====") 
            id_buscar = int(input("Digite o ID do chamado: "))  
            chamado = buscar_chamado(id_buscar) # chamado vai ser o dict do chamado_procurado 
            verificar_buscar(chamado) 
 
        case "3": 
            print("\n==== NOVO CHAMADO ====") 
            novo_cliente = input("Digite o nome do Cliente: ").strip().capitalize() 
            novo_categoria = input("Digite a categoria: ").strip().capitalize() 
            novo_prioridade = input("Digite a prioridade: ").strip().capitalize() 
            novo_descricao = input("Digite a descrição: ").strip().capitalize() 
            
            chamado = novo_chamado(novo_cliente, novo_categoria, novo_prioridade, novo_descricao) 
            print("Chamado Cadastrado Com Sucesso!") 
 
        case "4": 
            print() 
            id_buscar = int(input("Digite o ID do chamado: ")) 
            chamado = buscar_chamado(id_buscar) 
            
            if chamado: # se tiver algo dentro do dict 
                print("==== ALTERAR STATUS ====") 
                print("1 - Aberto") 
                print("2 - Em andamento") 
                print("3 - Resolvido") 
                
                status = input("Digite uma das opções: ") 
                alterar_status(status, chamado) 
            else: 
                print("Chamado Não Encontrado!") 
                
        case "5": 
            print("\n==== LISTA POR PRIORIDADE ====") 
            prioridade_buscar = input("Digite a prioridade: ").strip().capitalize() 
            print() 
            listar_prioridade(prioridade_buscar) 
            
        case "6": 
            print("\n==== LISTA POR STATUS ====") 
            status_buscar = input("Digite o status: ").strip().capitalize() 
            print() 
            listar_status(status_buscar) 
            
        case "7": 
            print("\n==== QUANTIDADE DE CHAMADAS POR CATEGORIA ====") 
            
            # Chama a função para criar um dict com a quantidade de chamados por categoria
            quantidade_categoria = contagem_por_categoria(chamados) 
            
            # Percorre o dict mostrando a categoria e a quantidade de chamados
            for k, v in quantidade_categoria.items(): 
                print(f"{k}: {v}") 
                
        case "8": 
            print("\n==== CHAMADO DE MAIOR PRIORIDADE ====") 
            
            # Chama a função que procura o chamado com maior prioridade
            chamado = maior_prioridade(chamados) 
            
            if chamado: 
                print(f"ID:{chamado['id']}") 
                mostrar_chamado(chamado) 
            else: 
                print("Nenhum chamado cadastrado.") 
                
        case "9": 
            print("\n==== ENCERRAR CHAMADO ====") 
            
            id_buscar = int(input("Digite o ID do chamado: ")) 
            chamado = buscar_chamado(id_buscar) 
            
            if chamado: 
                print(f"Id: {chamado['id']}") 
                mostrar_chamado(chamado) 
                
                r = input("O chamado está resolvido [s/n]?  ").strip().lower() 
                
                # Enquanto o usuário não digitar "s" ou "n", continua pedindo uma resposta válida
                while r not in ("s", "n"): 
                    r = input(" Tente Novamente! O chamado está resolvido [s/n]?  ").strip().lower() 
                
                # Envia a resposta e o chamado para a função responsável por encerrá-lo
                encerrar_chamado(r, chamado) 
            else: 
                print("Chamado Não Encontrado!") 
 
        case _: 
            print("Operação Inválida! Tente Novamente!")