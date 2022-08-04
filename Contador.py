from time import sleep


def lin():
    print('-=-'*15)


def contador(a, b, c):
    lin()
    if c < 0:
        c *= -1
    if c == 0:
        c = 1
    print(f'Contagem de {a} até {b} de {c} em {c}')
    if a < b:
        cont = a
        while cont <= b:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont += c
        print('FIM!')
    else:
        cont = a
        while cont >= b:
            print(f'{cont} ', end='')
            sleep(0.3)
            cont -= c
        print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
lin()
print('Agora é sua vez de personalizar a contagem.')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pss = int(input('Passo:  '))
contador(ini, fim, pss)
