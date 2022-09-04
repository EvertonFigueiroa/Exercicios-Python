def leiaa(a):
    while True:
        try:
            question = int(input(a))
        except (ValueError, TypeError):
            print('\033[4;49;91m ERRO! Digite um número inteiro válido!\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[4;49;91m Usúario preferiu não escolher!\033[m')
            return 0
        else:
            return question


n = leiaa('Dígite um número: ')
print(f'Você acabou de dígitar o número {n}')
