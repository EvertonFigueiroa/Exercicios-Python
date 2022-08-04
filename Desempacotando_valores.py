from time import sleep
from random import randint
lista = list()


def maior(* valores):
    print(f'Analisando os valores passados...')
    for c in valores:
        print(f'{c} ', end='', flush=True)
        sleep(0.5)
    print(f'foram informados {len(valores)} valores ao todo')
    if len(valores) == 0:
        print(f'O maior número é 0')
    else:
        print(f'O maior valor informado foi o {max(valores)}')
    print(f'-=' *20)

maior(randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60))
maior(randint(0, 60), randint(0, 60), randint(0, 60))
maior(randint(0, 60))
maior()
