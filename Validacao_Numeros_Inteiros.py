def leiaInt(a):
    question = input(a)
    while True:
        if question.isnumeric():
            question = int(question)
            return question
        else:
            if question.strip() == '' or question != int:
                print('\033[4;49;91m ERRO! Digite um número inteiro valido!\033[m')
                question = input(a)


n = leiaInt('Dígite um número: ')
print(f'Você acabou de dígitar o número {n}')
