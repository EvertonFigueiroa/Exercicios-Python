def fatorial(n, show=False):
    """
    -> Calcular o fatorial de um número.
    :param n: O valor a ser calculado.
    :param show: Mostra ou não o calculo.
    :return: Retorna o resultado da função.
    """

    if show == True:
        f = 1
        for c in range(n, 0, -1):
            print(f'{c}', end='')
            if c == 1:
                print(f' = ', end='')
            else:
                print(f' x ', end='')
            f *= c
        return f
    else:
        f = 1
        for c in range(n, 0, -1):
            f *= c
        return f


question = int(input('Dígite um número: '))
print(fatorial(question, show=False))
help(fatorial)

