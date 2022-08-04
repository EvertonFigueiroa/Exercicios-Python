valores = []
cont = 0
while True:
    valores.append(int(input('Dígite o valor: ')))
    cont += 1
    n = str(input('Deseja continuar? [S/N]'))
    if n in 'Nn':
        break
print(f'A lista possui {cont} elementos')
valores.sort(reverse=True)
print(f'A lista em ordem decrescente é {valores}')
if 5 in valores:
    print('A lista possui o elemento 5')
else:
    print('A lista não tem o 5')
