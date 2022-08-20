def leiaInt(a):
    while True:
        question = input(a)
        if question.isnumeric():
            question = int(question)
            return question
        else:
            if question.strip() == '' or question != int:
                print('\033[4;49;91m ERRO! Digite um número inteiro válido!\033[m')


n = leiaInt('Dígite um número: ')
print(f'Você acabou de dígitar o número {n}')
