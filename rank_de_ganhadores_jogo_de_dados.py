from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
acum = 0
print(f'{"Valores sorteados: ":<}')
for c in range(1, 5):
    jogadores[f'jogador{c}'] = randint(1, 6)
    print(f'    O jogador {c} tirou {jogadores[f"jogador{c}"]}')
    sleep(1)
print(f'Ranking dos jogadores: ')
jogadores = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for r, v in enumerate(jogadores):
    print(f"    {r+1}º Lugar: {v[0]} com {v[1]}")
    sleep(1)
