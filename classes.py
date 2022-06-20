


from uteis import *
from time import sleep

class Person:
    def __init__(self, nome, cpf, data_de_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.data_de_nascimento = data_de_nascimento

    def retornar_cpf(self):
        return self.cpf
    
    def novo_nome(self):
        while True:
            try:
                nome = str(input('Digite o Novo Nome do Usuário: '))
            except ValueError:
                print('\033[31mErro, Tente Novamente\033[m')
            else:
                break
        self.nome = nome

    def novo_cpf(self):
        while True:
            try:
                cpf = str(input('Digite o Novo CPF do Usuário: '))
            except ValueError:
                print('\033[31mErro, Tente Novamente\033[m')
            else:
                break
        self.cpf = cpf

    def nova_data(self):
        while True:
            try:
                data = str(input('Digite a Nova Data de Nascimento do Usuário: '))
            except ValueError:
                print('\033[31mErro, Tente Novamente\033[m')
            else:
                break
        self.data_de_nascimento = data

    def retornar_info(self):
        return self.nome, self.cpf, self.data_de_nascimento



class Bd:
    def __init__(self):
        self.banco_de_dados = []

    def cadastro_bd(self):
        nome, cpf, data = cadastro_informacoes()
        find = False
        for cadastro in self.banco_de_dados:
            if cadastro.retornar_cpf() == cpf:
                find = True
                print('Usuário Já Cadastrado no Banco de Dados')
                print('Retornando ao Menu...')
                sleep(1)
        if not find:
            self.banco_de_dados.append(Person(nome, cpf, data))
            print('Usuário Cadastrado com Sucesso no Banco de Dados')
            print('Retornando ao Menu...')
            sleep(1)
    
    def editar_nome(self):
        cpf = inserir_cpf()
        find = False
        for cadastro in self.banco_de_dados:
            if cadastro.retornar_cpf() == cpf:
                find = True
                cadastro.novo_nome()
                print('Nome do Usuário Alterado com Sucesso')
                print('Retornando ao Submenu...')
                sleep(1)
        if not find:
            print('CPF não Cadastrado no Banco de Dados')
            print('Retornando ao Submenu...')
            sleep(1)

    def editar_cpf(self):
        cpf = inserir_cpf()
        find = False
        for cadastro in self.banco_de_dados:
            if cadastro.retornar_cpf() == cpf:
                find = True
                cadastro.novo_cpf()
                print('CPF de Usuário Alterado com Sucesso')
                print('Retornando ao Submenu...')
                sleep(1)
        if not find:
            print('CPF não Cadastrado no Banco de Dados')
            print('Retornando ao Submenu...')
            sleep(1)

    def editar_data(self):
        cpf = inserir_cpf()
        find = False
        for cadastro in self.banco_de_dados:
            if cadastro.retornar_cpf() == cpf:
                find = True
                cadastro.nova_data()
                print('Data de Aniversário do Usuário Alterada com Sucesso')
                print('Retornando ao Submenu...')
                sleep(1)
        if not find:
            print('CPF não Cadastrado no Banco de Dados')
            print('Retornando ao Submenu...')
            sleep(1)

    def mostrar_info(self):
        cpf = inserir_cpf()
        find = False
        for cadastro in self.banco_de_dados:
            if cadastro.retornar_cpf() == cpf:
                find = True
                nome, cpf_data, data_de_nascimento = cadastro.retornar_info()
                print('-=-' * 10)
                print('Dados de Usuário:'.center(30))
                print(f'Nome: {nome}')
                print(f'CPF: {cpf_data}')
                print(f'Data de Nascimento: {data_de_nascimento}')
                print('-=-' * 10)
                str(input('Digite Qualquer Coisa Para Voltar ao Menu: '))
                print('Retornando ao Menu...')
                sleep(1)
        if not find:
            print('CPF não Cadastrado no Banco de Dados')
            print('Retornando ao Menu...')
            sleep(1)

    def apagar_cadastro(self):
        cpf = inserir_cpf()
        find = False
        for index, cadastro in enumerate(self.banco_de_dados):
            if cadastro.retornar_cpf() == cpf:
                find = True
                self.banco_de_dados.pop(index)
                print('Dados de Usuário Apagados do Banco de Dados')
                print('Retornando ao Menu...')
                sleep(1)
        if not find:
            print('CPF não Cadastrado no Banco de Dados')
            print('Retornando ao Menu...')
            sleep(1)
                    

    