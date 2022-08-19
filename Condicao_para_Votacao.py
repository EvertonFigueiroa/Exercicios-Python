print('-=-=-=-=-= Aptidão para votação =-=-=-=-=-')


def voto(ano):
    from datetime import date
    ano = date.today().year - question
    if ano < 18:
        return f'Você tem {ano} anos e NÃO pode votar!'
    elif 65 > ano >= 18:
        return f'Você tem {ano} anos e é OBRIGATÓRIO votar!'
    elif 16 <= ano < 18 or ano > 65:
        return f'Você tem {ano} anos e seu voto é OPICIONAL'


question = int(input('Qual seu ano de nascimento?: '))
print(voto(question))
