print('-=-=-=-=-=-=BOLETIM ESCOLAR=-=-=-=-=-=-')
boletim = []
ef = []
nota = []
while True:
    ef.append(str(input('Nome do aluno: ')).strip().title())
    nota.append(float(input('Nota 1: ')))
    nota.append(float(input('Nota 2: ')))
    ef.append(nota[:])
    boletim.append(ef[:])
    ef.clear()
    nota.clear()
    dec = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    while True:
        if dec not in 'SN':
            print('Opção invalida, tente novamente!')
            dec = str(input('Deseja continuar? [S/N]: ')).strip().upper()
        else:
            break
    if dec == 'N':
        break
print(f'{"Posição":.^13}{"Aluno":.^13}{"Média":.^13}')
for c, v in enumerate(boletim):
    print(f'{c:^13}', end='')
    print(f'{v[0]:^13}', end='')
    print(f'{(v[1][0]+v[1][1])/2:^13}')
print(f'{"":.^39}')
while True:
    print()
    r = int(input('Digite a posição do aluno para saber suas notas\ncaso não queira digite [999]: '))
    if r == 999:
        print('Encerrando...')
        break
    if r <= (len(boletim)-1):
        print()
        print(f'As notas de {boletim[r][0]} são {boletim[r][1]}')
    else:
        print('Opção invalida, tente novamente!')
