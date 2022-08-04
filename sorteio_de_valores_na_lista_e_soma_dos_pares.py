from time import sleep
from random import randint


def sorteia(numeros):
    print(f'Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        numeros.append(randint(0, 60))
    for c in numeros:
        print(f'{c} ', end='')
        sleep(0.5)
    print('FIM!')


def somapar(numeros):
    pares = 0
    for c in numeros:
        if c % 2 == 0:
            pares += c
    print(f'Somando os valores pares de {numeros}, temos {pares}')


lista = list()
sorteia(lista)
somapar(lista)
