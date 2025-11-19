from datetime import datetime
#import json
#import pandas
#import flask
#banco de dados
from time import sleep
depositos = []
saques = []
cofrinho = []
valor_conta = 0

def Mostrar_Menu():
    print('-=' * 25)
    print(f'{"MENU PRINCIPAL":^50}')
    print('-=' * 25)
    print('''
[1] Nova transação        ||  [5] Ver saldo do cofrinho
[2] Ver saldo             ||  [6] Adicionar ao Cofrinho
[3] Ver transações        ||  [7] Retirar do Cofrinho
[4] Criar Cofrinho        ||  [8] Sair 
''')
    print('-=' * 25)

def escolher_opcao():
      while True:
            try:
                opcao = int(input('Digite sua opção: '))
                if opcao in [1,2,3,4,5,6,7,8]:
                    return opcao
                else:
                    print('Erro! Digite um valor válido')
            except ValueError:
                print('Erro! Digite apenas números.')
            continue

def escolher_tipo_transacao():
    print('[1] Para Adicionar \n[2] Para retirar')
    try:
        opcao_transacao = int(input('Escolha sua opção: '))
    except ValueError:
        print('Erro de valor')

    try:
        if opcao_transacao in [1, 2]:
            return opcao_transacao
        else:
            print('Erro! Digite um valor válido.')
    except ValueError:
        print('Erro! Digite apenas Números.')

def criando_cofrinho():
    global valor_conta
    nome_cofre = str(input('Qual será o nome do seu cofrinho? ')).strip()
    meta_cofre = float(input('Qual meta você quer definir para esse cofrinho? R$'))
    valor_inicial_cofrinho = float(input('Qual valor inicial você deseja colocar no cofre? R$'))
    if valor_inicial_cofrinho > valor_conta:
        print('Você Não possui esse saldo na conta, o valor inicial será R$00,00')
        valor_inicial_cofrinho = 0
    else:
        valor_conta -= valor_inicial_cofrinho
    criacao_cofrinho = {'nome': nome_cofre, 'meta': meta_cofre, 'valor': [valor_inicial_cofrinho]}
    cofrinho.append(criacao_cofrinho)
         


while True:
    Mostrar_Menu()
    opcao = escolher_opcao()
    if opcao == 1:
        data_atual = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        tipo = escolher_tipo_transacao()
        valor = float(input('Digite o valor: R$'))
        try:    
            if tipo == 1:
                valor_conta += valor
                print('CONFIRMANDO...')
                transacao = {'data': data_atual, 'valor': valor}
                depositos.append(transacao)
                sleep(2)
                print('Valor adicionado com sucesso')
            elif tipo == 2:
                if valor > valor_conta:
                    print('Analisando...')
                    sleep(2)
                    print('Você não possui saldo')                   
                    continue    
                else:
                    valor_conta -= valor
                    print('CONFIRMANDO...')
                    transacao = {'data': data_atual, 'valor': valor}
                    saques.append(transacao)
                    sleep(2)
                    print('Valor retirado com sucesso')

            else:
                print('Houve um erro, o programa voltará do inicio.')
                continue
        except ValueError:
            print('Houve um erro, o programa voltará do inicio.')
            continue

    elif opcao == 2:
        print(f"Seu saldo atual é de R${valor_conta:.2f}")
        sleep(1)
        continue

    elif opcao == 3:
        print('[1] Para ver depositos \n[2] Para ver saques \n[3] Para voltar ao menu')
        opcao_transacoes = int(input('Escolha:'))
        if opcao_transacoes == 1:
            if len(depositos) == 0:
                print('Você não possui depositos')
            else:
                print('Esses foram seus depositos: ')
                for itens in depositos:
                    print(f"Data: {itens['data']} | Valor: R${itens['valor']:.2f}")
        elif opcao_transacoes == 2:
            if len(saques) == 0:
                print('Você não possui saques')
            else:
                print('Esses foram seus saques:')
                for itens in saques:
                    print(f"Data: {itens['data']} | Valor: {itens['valor']:.2f}")
        elif opcao_transacoes == 3:
            continue

    elif opcao == 4:
        print('Analisando...')
        sleep(1.3)
        if len(cofrinho) < 3:
            criando_cofrinho()
        else:
            print('Você atingiu o limite de cofrinhos que pode ter. ')
            continue

    elif opcao == 5:
        for pos, itens in enumerate(cofrinho):
            print(f"[{pos+1}] {itens['nome']}")

        escolha_cofre_saldo = int(input("Qual cofrinho você deseja escolher? "))
        indice_cofre_saldo = escolha_cofre_saldo - 1

        if 0 <= indice_cofre_saldo < len(cofrinho):
            cofre = cofrinho[indice_cofre_saldo]
            print(f"O saldo do cofrinho {cofre['nome']} é R${sum(cofre['valor']):.2f}")
        else:
            print("Opção inválida.")
            continue

    elif opcao == 6:
        if len(cofrinho) > 0:
            for pos, itens in enumerate(cofrinho):
                print(f"[{pos+1}] {itens['nome']}")
            escolha_adicionar_saldoCofre = int(input('Em qual cofre você deseja adicionar dinheiro? '))
            indice_adicionar_cofre = escolha_adicionar_saldoCofre - 1

            if 0 <= indice_adicionar_cofre < len(cofrinho):
                adicionar_valor_cofrinho = float(input('Quanto deseja adicionar? R$'))
                if adicionar_valor_cofrinho < valor_conta:
                    cofrinho[indice_adicionar_cofre]['valor'].append(adicionar_valor_cofrinho)
                    valor_conta -= adicionar_valor_cofrinho
                    print('Valor adicionado com sucesso!')
                else:
                    print('Você não possui saldo na sua conta')
            else:
                print('Houve um erro!')
                continue
        else:
            print('Você ainda não possui um cofrinho')

    elif opcao == 7:
        if len(cofrinho) > 0:
            for pos, itens in enumerate(cofrinho):
                print(f"[{pos+1}] {itens['nome']}")
            escolha_remover_saldoCofre = int(input('Em qual cofre você deseja remover dinheiro? '))
            indice_remover_cofre = escolha_remover_saldoCofre - 1

            if 0 <= indice_remover_cofre < len(cofrinho) and sum(cofrinho[indice_remover_cofre]['valor']) > 0:
                valor_remover = float(input("Quanto deseja retirar? R$"))
                valor_conta += valor_remover

                if valor_remover <= sum(cofrinho[indice_remover_cofre]['valor']):
                    cofrinho[indice_remover_cofre]['valor'].append(-valor_remover)
                    print('Valor retirado com sucesso')
                else:
                    print('Você não possui saldo suficiente nesse cofrinho.')
            else:
                print('Opção invalida ou cofrinho sem saldo')
        else:
            print('Você ainda naõ possui um cofrinho')

    elif opcao == 8:
        print('Saindo...')
        sleep(1.3)   
        break

print('Programa finalizado')