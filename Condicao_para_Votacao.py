from datetime import date
print('-=-=-=-=-= Aptidão para votação =-=-=-=-=-')


def voto(ano):
    ano = date.today().year - question
    if ano < 18:
        print(f'Você tem {ano} anos e NÃO pode votar!')
    elif 65 > ano >= 18:
        print(f'Você tem {ano} anos e é OBRIGATÓRIO votar!')
    else:
        print(f'Você tem {ano} anos e seu voto é OPICIONAL')

    return ano


question = int(input('Qual seu ano de nascimento?: '))
answer = voto(question)
