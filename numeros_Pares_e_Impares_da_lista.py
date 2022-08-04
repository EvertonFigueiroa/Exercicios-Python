l1 = list()
l2 = list()
l3 = list()
while True:
    l1.append(int(input('Digite um número: ')))
    d = str(input('Deseja continuar [S/N]'))
    if d in 'Nn':
        break
c = 0
for c in l1:
    if c % 2 == 0:
        l2.append(c)
    else:
        l3.append(c)
print(f'A lista completa é {l1}')
print(f'A lista com números páres é {l2}')
print(f'A lista com números ímpares é {l3}')
