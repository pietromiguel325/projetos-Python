from veiculo import CarroPasseio, Caminhao
from seguro import SeguroBasico, SeguroPremium
from exceptions import LocadoraException, VeiculoIndisponivelError
from auditoria import Auditoria

def tipos_vei_disponiveis():
    tipos = {'1': 'Carro Para Passeio', '2': 'Caminhão'}
    print("\n--- OPÇÕES ---")
    for k, v in tipos.items():
        print(f"[{k}] - {v}")
    escolha = input("Escolha uma das opções [1] ou [2]: ")
    while escolha not in tipos:
        escolha = input("Por Favor! Escolha uma das opções [1] ou [2]: ")
    return tipos[escolha]

def tipos_seg():
    tipos = {'1': 'Seguro Básico', '2': 'Seguro Premium'}
    print("--- OPÇÕES ---")
    for k, v in tipos.items():
        print(f"[{k}] - {v}")
    escolha = input("Escolha uma das opções [1] ou [2]: ")
    while escolha not in tipos:
        escolha = input("Por Favor! Escolha uma das opções [1] ou [2]: ")
    return tipos[escolha]


frota = dict()

while True:
    print("\n=== MENU ===")
    print("[1] Cadastrar Veículo")
    print("[2] Alugar Veículo")
    print("[3] Devolver Veículo")
    print("[4] Exibir Relatório Financeiro & Frota")
    print("[5] Sair")
    print("=" * 12)
    opcao = input("Escolha uma das opções: ")
    print()
    match opcao:
        case "1":
            tipo_seguro = tipos_seg()
            if tipo_seguro == 'Seguro Básico':
                seguro = SeguroBasico()
            else:
                seguro = SeguroPremium()
            print()
            placa = input("Digite a placa: ").strip().upper()
            while len(placa) != 7:
                placa = input("Digite a placa: ").strip().upper()
            modelo = input("Digite o modelo: ").strip()
            while True:
                try:
                    valor_diaria = input("Digite o valor da diária: ")
                    valor_diaria = float(valor_diaria)
                    if valor_diaria > 0:
                        break
                except ValueError:
                    print("Valor Inválido!")
            tipo_veiculo = tipos_vei_disponiveis()
            if tipo_veiculo == "Carro Para Passeio":
                veiculo = CarroPasseio(placa, modelo, valor_diaria, seguro)
            else:
                while True:
                    try:
                        carga_ton = input("Digite a capacidade de carga: ")
                        carga_ton = float(carga_ton)
                        if carga_ton > 0:
                            break
                    except ValueError:
                        print("Valor Inválido!")
                veiculo = Caminhao(placa, modelo, valor_diaria, seguro, carga_ton)
            frota[veiculo.placa] = veiculo

        case "2":
            for i, (placa, veiculo) in enumerate(frota.items(), start=1):
                print(f"[{i}] - Placa: {placa} | Modelo: {veiculo.modelo} | Alugado: {veiculo.alugado}")
            escolha = input("Digite a placa do veículo: ").strip().upper()
            if escolha in frota:
                while True:
                    try:
                        dias = input("Digite Quantos Dias Deseja Alugar: ")
                        dias = int(dias)
                        break
                    except ValueError:
                        print(f"Valor Inválido! Valor Digitado: {dias}")

                valor_aluguel = frota[escolha].calcular_aluguel(dias)
                valor_aluguel_seguro = frota[escolha].calcular_aluguel_seguro(dias)
                print(f"O valor sem o seguro: R${valor_aluguel:.2f}")
                print(f"O valor com o seguro: R${valor_aluguel_seguro:.2f}")

                valor_escolha = input("Digite um dos dois [SEM SEGURO]/[COM SEGURO]: ").strip().upper()
                while valor_escolha not in ("SEM SEGURO", "COM SEGURO"):
                    valor_escolha = input("Por favor! Digite uma das opções [SEM SEGURO]/[COM SEGURO]: ").strip().upper()
                if valor_escolha == 'SEM SEGURO':
                    valor_total = valor_aluguel
                else:
                    valor_total = valor_aluguel_seguro

                r = str(input("Deseja alugar [S/N]? ")).strip().upper()
                while r not in ('S', 'N'):
                    r = str(input("Digite Novamente! Deseja alugar [S/N]? ")).strip().upper()
                if r == 'S':
                    try:
                        frota[escolha].alugar()
                        Auditoria.registrar_locacao(frota[escolha], dias, valor_total)
                    except VeiculoIndisponivelError as e:
                        print(f"[ERRO] {e}")
                else:
                    print("Operação Cancelada!")
            else:
                print("Veículo Não Encontrado!")

        case "3":
            for i, (placa, veiculo) in enumerate(frota.items(), start=1):
                print(f"[{i}] - Placa: {placa} | Modelo: {veiculo.modelo} | Alugado: {veiculo.alugado}")
            escolha = input("Digite a placa do veículo: ").strip().upper()
            if escolha in frota:
                while True:
                    try:
                        km_percorridos = input("Digite Quando KM percorreu: ")
                        km_percorridos = float(km_percorridos)
                        break
                    except ValueError:
                        print(f"Valor Inválido! Valor Digitado: {km_percorridos}")
                try:
                    frota[escolha].devolver(km_percorridos)
                except LocadoraException as e:
                    print(f"[ERRO] {e}")
            else:
                print("Veículo Não Encontrado!")

        case "4":
            Auditoria.exibir_balanco()

        case "5":
            break

        case _:
            print("[ERRO] Escolha uma das Opções!")