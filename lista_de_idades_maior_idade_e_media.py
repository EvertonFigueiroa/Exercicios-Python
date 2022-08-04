pessoas = list()
dados = dict()
acum = 0
while True:
    dados['nome'] = str(input('Nome: ')).strip().title()
    dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
    while True:
        if dados['sexo'] not in 'MF' or dados['sexo'] == '':
            print(f'ERRO!! Escolha M ou F')
            dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()
        else:
            break
    dados['idade'] = int(input('Idade: '))
    pessoas.append(dados.copy())
    new = str(input('Desejar continuar: [S/N] ')).strip().upper()
    while True:
        if new not in 'SN':
            print('ERRO! Escolha S ou N')
            new = str(input('Desejar continuar: [S/N] ')).strip().upper()
        else:
            break
    if new in 'N':
        break
print('-=-'*20)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
for c in pessoas:
    acum += c['idade']
print(f'B) A média de idade é {acum/len(pessoas):.0f} anos.')
print(f'C) As mulheres cadastradas foram ', end='')
for c in pessoas:
    if c['sexo'] == 'F':
        print(f'{c["nome"]}', end=' ')
print(f'\nD) Lista de pessoas que estão acima da média: ')
for c in pessoas:
    if c['idade'] > (acum/len(pessoas)):
        print(f'nome = {c["nome"]}; sexo = {c["sexo"]}; idade = {c["idade"]};')
print(f'-=- ENCERRADO -=-')
