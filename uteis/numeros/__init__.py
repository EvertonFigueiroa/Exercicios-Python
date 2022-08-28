def fatorial(n=0, ft=True):
    """
    -> Calculo para fatorial
    :param n: valor do input
    :param ft: Opcional se quer o valor com duas casas decimais
    :return: retorna o resultado da função
    """
    f = 1
    for c in range(1, n+1):
        f *= c
    if ft:
        f = valor(f)
    return f


def dobro(n=0, ft=True):
    """
    -> Calculo do dobro do valor
    :param n: valor do input
    :param ft: Opcional se quer o valor com duas casas decimais
    :return: retorna o resultado da função
    """
    f = n * 2
    if ft:
        f = valor(f)
    return f


def triplo(n=0, ft=True):
    """
    -> Calcula o triplo do valor
    :param n: valor do input
    :param ft: Opcional se quer o valor com duas casas decimais
    :return: retorna o resultado da função
    """
    f = n * 3
    if ft:
        f = valor(f)
    return f


def aumentar(n=0, m=0, ft=True):
    """
    -> Aumenta o valor em quantos porcentos escolher
    :param n: valor do input
    :param m: Quantos porcentos deseja aumentar
    :param ft: Opcional se quer o valor com duas casas decimais
    :return: retorna o resultado da função
    """
    v2 = (n*m)/100
    f = n+v2
    if ft:
        f = valor(f)
    return f


def metade(n=0, ft=True):
    """
    -> Dívide o input por dois
    :param n: valor do input
    :param ft: Opcional se quer o valor com duas casas decimais
    :return: retorna o resultado da função
    """
    f = n / 2
    if ft:
        f = valor(f)
    return f


def diminuir(n=0, m=0, ft=True):
    """
    -> Diminui o valor em quantos porcentos escolher
    :param n: valor do input
    :param m: Quantos porcentos deseja diminuir
    :param ft: Opcional se quer o valor com duas casas decimais
    :return: retorna o resultado da função
    """
    v2 = (n * m) / 100
    f = n - v2
    if ft:
        f = valor(f)
    return f


def valor(n=0, md="R$"):
    """
    -> Função para formatar um número para valor em real
    :param n: valor do input
    :param md: coloca o real
    :return: retorna o resultado da função
    """
    f = f'{md}{n:.2f}'.replace(".", ",")
    return f


def resumo(n, a=0, b=0):
    """
    -> Resumo de todas as funções de números
    :param n: valor do input
    :param a: Quantidade de porcentagem para aumentar
    :param b: Quantidade de porcentagem para diminuir
    """
    print('='*32)
    print(f'RESUMO DE VALORES'.center(32))
    print('=' * 32)
    print(f'Preço analisado: \t{valor(n)}')
    print(f'Dobro do preço: \t{dobro(n)}')
    print(f'Metado do preço: \t{metade(n)}')
    print(f'{a}% de aumento: \t{aumentar(n, a)}')
    print(f'{b}% de redução: \t{diminuir(n, b)}')
    print('=' * 32)
