from datetime import datetime
data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

from time import sleep
depositos = []
saques = []
valor_conta = 0
cofrinho = 0
def Mostrar_Menu():
        print('-='*20)
        print('''[1] Nova transação
[2] Ver saldo
[3] Ver transações
[4] Adicionar ao Cofrinho
[5] Ver saldo do cofrinho
[6] Sair         
''')

def escolher_opcao():
      while True:
            try:
                opcao = int(input('Digite sua opção: '))
                if opcao in [1,2,3,4,5,6]:
                    return opcao
                else:
                    print('Erro! Digite um valor válido')
            except ValueError:
                print('Erro! Digite apenas números.')
            continue
def escolher_tipo_transacao():
    print('[1] Para Adicionar \n[2] Para retirar')
    opcao_transacao = int(input('Escolha sua opção: '))
    try:
        if opcao_transacao in [1, 2]:
            return opcao_transacao
        else:
            print('Erro! Digite um valor válido.')
    except ValueError:
        print('Erro! Digite apenas Números.')
     

while True:
    Mostrar_Menu()
    opcao = escolher_opcao()
    if opcao == 1:
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
        except:
            print('Houve um erro, o programa voltará do inicio.')
            continue

    elif opcao == 2:
        print(f'Seu saldo atual é de R${valor_conta:.2f}')
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
                    print(f'Data:{transacao['data']} | Valor: {transacao['valor']}')
        elif opcao_transacoes == 2:
            if len(saques) == 0:
                print('Você não possui saques')
            else:
                print('Esses foram seus saques:')
                for itens in saques:
                    print(f'Data: {transacao['data']} | Valor: {transacao['valor']}')
        elif opcao_transacoes == 3:
            continue

    elif opcao == 4:
        valor_cofrinho = float(input('Quanto deseja adicionar ao cofrinho? R$'))
        print('CONFIRMANDO...')
        sleep(1.5)
        if valor_cofrinho <= valor_conta:
            cofrinho += valor_cofrinho
            valor_conta -= valor_cofrinho
            print('Valor adicionado com sucesso.')
            continue
        else:
            print('Você não possui esse valor na sua conta.')
            continue

    elif opcao == 5:
        print(f'Você possui R${cofrinho} no seu cofrinho')
        continue

    elif opcao == 6:
        print('Saindo...')
        sleep(2)   
        break

print('Programa finalizado')