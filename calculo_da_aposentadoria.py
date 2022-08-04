from datetime import date
trampo = dict()
trampo['nome'] = str(input('Nome: ')).strip().title()
trampo['idade'] = int(input('Ano de nascimento: '))
trampo['ctps'] = int(input('Número da carteira de trabalho (0 se não tiver): '))
if trampo['ctps'] != 0:
    trampo['contratação'] = int(input('Ano de contratação: '))
    trampo['salário'] = float(input('Salário: R$'))
    trampo['aposentadoria'] = ((trampo['contratação'] - trampo['idade']) + 35)
trampo['idade'] = (date.today().year - trampo['idade'])
print(f'-=-'*18)
for c, v in trampo.items():
    print(f'- {c} tem o valor {v} ')
print(trampo.items())
