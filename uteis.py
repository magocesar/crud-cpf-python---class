

def cadastro_informacoes():
    while True:
        try:
            nome = str(input('Digite o Nome do Usuário: ')).strip().upper()
        except ValueError:
            print('\033[31mErro, Tente Novamente\033[m')
        else:
            break
    while True:
        try:
            cpf = str(input('Digite o CPF do Usuário: ')).strip().upper()
        except ValueError:
            print('\033[31mErro, Tente Novamente\033[m')
        else:
            break
    while True:
        try:
            data = str(input('Digite a Data de Nascimento do Usuário: ')).strip().upper()
        except ValueError:
            print('\033[31mErro, Tente Novamente\033[m')
        else:
            break
    return nome, cpf, data


def inserir_cpf():
    while True:
        try:
            cpf = str(input('Digite o CPF do Usuário: ')).strip().upper()
        except ValueError:
            print('\033[31mErro, Tente Novamente\033[m')
        else:
            break
    return cpf
