def ajuda(a):
    while True:
        print(f'\033[3;43;3m\033[1;30m{"~~":~^25}')
        print(f'{"SISTEMA DE AJUDA PyHELP":^25}')
        print(f'{"~~":~^25}''\n\033[m')
        question = str(input(a))
        if question == 'fim':
            break
        print(f'\033[3;44;3m\033[1;30m{"~~":~^25}')
        print(f'{f"Acessando o manual do {question}":^25}')
        print(f'{"~~":~^25}''\n\033[m')
        print('\033[1;107m\033[1;30m')
        help(question)
        print('\033[1;107m\033[1;30m')


a = ajuda('Função ou Biblioteca > ')

