def sovalores(n):
    """
    -> Função para validação de números-valores em real
    :param n: valor do input
    :return: retorna o resultado da função
    """
    while True:
        question = str(input(n)).replace(",", ".")
        f = question
        if question.isalpha() or question.strip() == '':
            print(f'\033[4;49;91m ERRO! você dígitou "{f}" dígite apenas valores monetários!\033[m')
        else:
            return float(question)


def menu():
    print('='*40)
    print('MENU PRINCIPAL'.center(40))
    print('=' * 40)
    print('\033[3;49;93m1\033[m - \033[3;49;94mVer pessoas cadastradas\033[m \n'
          '\033[3;49;93m2\033[m - \033[3;49;94mCadastrar nova pessoa\033[m \n'
          '\033[3;49;93m3\033[m - \033[3;49;94mSair do sistema\033[m')
    print('=' * 40)
    f = leiaInt('\033[3;49;92mSua Opção: \033[m')
    return f



def linhas():
    print(f'='*40)


def leiaInt(a):
    while True:
        question = input(a)
        if question.isnumeric():
            question = int(question)
            return question
        else:
            if question.strip() == '' or question != int:
                print('\033[4;49;91m ERRO! Digite um número inteiro válido!\033[m')

