l1 = list()
l2 = list()
pes = list()
lev = list()
pm = 0
pme = 999
while True:
    l1.append(str(input('Digite seu nome: ')))
    l1.append(int(input('Digite seu peso: ')))
    l2.append(l1[:])
    l1.clear()
    p = str(input('Deseja continuar? [S/N]'))
    if p in 'Nn':
        break
for c in l2:
    if c == 0:
        pm = c[1]
    if c[1] >= pm:
        pm = c[1]
    if c[1] <= pme:
        pme = c[1]
print(f'A quantidade de pessoas cadastradas é {len(l2)}')
print(f'O maior peso foi de {pm} e as pessoas pesadas são: ', end='')
for j in l2:
    if j[1] >= 99:
        print(f'[{j[0]}]')
print(f'O menor peso foi de {pme} e as pessoas leves são: ', end='')
for j in l2:
    if j[1] <= 98:
        print(f'[{j[0]}]')
