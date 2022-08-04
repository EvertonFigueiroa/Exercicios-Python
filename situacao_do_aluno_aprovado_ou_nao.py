boletim = dict()
boletim['nome'] = str(input('Nome: '))
boletim['média'] = float(input(f'Média de {boletim["nome"]}: '))
print(f'O nome é igual a {boletim["nome"]}')
print(f'A média é igual a {boletim["média"]}')
if boletim['média'] < 7:
    print(f'A situação é igual a Reprovado!')
else:
    print(f'Situação é igual a Aprovado')
