futebol = dict()
gols = list()
geral = list()
while True:
    acum = 0
    gols.clear()
    futebol.clear()
    futebol['nome'] = str(input('Nome do jogador: ')).strip().title()
    partidas = int(input(f'Quantas partidas {futebol["nome"]} jogou: '))
    for c in range(partidas):
        gols.append(int(input(f'Quantos gols na partida {c}: ')))
        acum += gols[-1]
    futebol['gols'] = gols.copy()
    futebol['total'] = acum
    geral.append(futebol.copy())
    r = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
    elif r not in 'SN':
        print('ERRO! Digite S ou N ')
        r = str(input('Deseja continuar: [S/N] ')).strip().upper()[0]
print('-=-'*20)
print('cod ', end='')
for i in futebol.keys():
    print(f'{i:<15}', end='')
print()
for c, v in enumerate(geral):
    print(f'{c:>2}', end='')
    for d in v.values():
        print(f' {str(d):<15}', end='')
    print()
print('-=-'*20)
while True:
    print()
    r = int(input('Mostrar dados de qual jogador (999 para parar): '))
    if r == 999:
        print('Encerrando...')
        break
    if r <= (len(geral)-1):
        print()
        print(f'-- Levanemnto do jogador {geral[r]["nome"]}: ')
        for c in range(len(geral[r]['gols'])):
            print(f'  Na partida {c+1} fez {geral[r]["gols"][c]}')
    else:
        print('Opção invalida, tente novamente!')
