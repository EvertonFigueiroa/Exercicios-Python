futebol = dict()
gols = list()
acum = 0
futebol['nome'] = str(input('Nome do jogador: ')).strip().title()
partidas = int(input(f'Quantas partidas {futebol["nome"]} jogou: '))
for c in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {c}: ')))
    acum += gols[-1]
futebol['gols'] = gols.copy()
futebol['total'] = acum
print('-=-'*20)
print(futebol)
print('-=-'*20)
for i, v in futebol.items():
    print(f'O campo {i} tem o valor {v}')
print('-=-'*20)
print(f'O jogador {futebol["nome"]} jogou {partidas} partidas.')
for i, v in enumerate(futebol['gols']):
    print(f' => Na partida {i}, fez {v} gols. ')
print(f'Foi um total de {partidas} gols')
