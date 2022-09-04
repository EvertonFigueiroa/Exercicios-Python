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


def menu(a=0):
    print('='*30)
    print('MENU PRINCIPAL'.center(30))
    print('=' * 30)
    print('\033[3;49;93m1\033[m - \033[3;49;94mVer pessoas cadastradas\033[m \n'
          '\033[3;49;93m2\033[m - \033[3;49;94mCadastrar nova pessoa\033[m \n'
          '\033[3;49;93m3\033[m - \033[3;49;94mSair do sistema\033[m')
    print('=' * 30)
    question = int(input('\033[3;49;92mSua opção: \033[m'))
    return question

