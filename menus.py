
# MENU DE OPÇÕES

from time import sleep
from main import banco_de_dados

def menu():
    from time import sleep
    from main import banco_de_dados
    ops = ('[1] - Cadastrar Usuários',
    '[2] - Editar Dados',
    '[3] - Mostrar Dados Indivíduais',
    '[4] - Apagar Usuário do Banco de Dados',
    '[5] - Sair do Programa')
    while True:
        print('-=-' * 10)
        print('CRUD DE USUÁRIOS'.center(30))
        print('-=-' * 10)
        print('Funções:'.center(30))
        for op in ops:
            print(op)
        print('-=-' * 10)
        try:
            ask = int(input('Digite uma Opção Válida: '))
        except ValueError:
            print('\033[31mErro, Tente Novamente\033[m')
        else:
            if ask not in [1, 2, 3, 4, 5]:
                print('\033[31mOpção Inválida\033[m')
            else:
                if ask == 1:
                    banco_de_dados.cadastro_bd()
                elif ask == 2:
                    sub_menu()
                elif ask == 3:
                    banco_de_dados.mostrar_info()
                elif ask == 4:
                    banco_de_dados.apagar_cadastro()
                elif ask == 5:
                    print('Até Breve!')
                    sleep(1)     
                    break

def sub_menu():
    from time import sleep
    from main import banco_de_dados
    ops = ('[1] - Editar Nome',
    '[2] - Editar CPF',
    '[3] - Editar Data de Nascimento',
    '[4] - Voltar')
    while True:
        print('-=-' * 10)
        print('EDITAR CADASTRO'.center(30))
        print('-=-' * 10)
        print('Funções:'.center(30))
        for op in ops:
            print(op)
        print('-=-' * 10)
        try:
            ask = int(input('Digite uma Opção Válida: '))
        except ValueError:
            print('\033[31mErro, Tente Novamente\033[m')
        else:
            if ask not in [1, 2, 3, 4]:
                print('\033[31mOpção Inválida\033[m')
            else:
                if ask == 1:
                    banco_de_dados.editar_nome()
                elif ask == 2:
                    banco_de_dados.editar_cpf()
                elif ask == 3:
                    banco_de_dados.editar_data()
                elif ask == 4:
                    print('Retornando ao Menu Inicial...')
                    sleep(1)
                    break        
    



