from time import sleep
from random import randint
listap = []
listae = []
print(f'{" Jogo da mega ":=^41}')
n = int(input('Quantos jogos você deseja?: '))
for c in range(0, n):
    for i in range(0, 6):
        listae.append(randint(1, 60))
    listap.append(listae[:])
    listae.clear()
print(f'{f" -=-=-=-=--< Sorteando {n} Jogos >-=-=-=-=-- "}')
for c in range(0, n):
    print(f' Jogo {c+1}: {listap[c]}')
    sleep(1)
print(' -=-=-=-=-=-=-< BOA SORTE! >=-=-=-=-=-=-=- ')
