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
