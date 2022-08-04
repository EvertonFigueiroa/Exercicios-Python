listap = list()
listae = list()
cont = cont1 = cont2 = cont3 = 0
for c in range(0, 3):
    listae.append(int(input(f'Digite um valor para [0, {c}]: ')))
listap.append(listae[:])
listae.clear()
for c in range(0, 3):
    listae.append(int(input(f'Digite um valor para [1, {c}]: ')))
listap.append(listae[:])
listae.clear()
for c in range(0, 3):
    listae.append(int(input(f'Digite um valor para [2, {c}]: ')))
listap.append(listae[:])
listae.clear()
print(f'-=-'*20)
for c in listap:
    for i, v in enumerate(c):
        print(f'[{v:^5}]', end='')
        if i == 2:
            print('\n', end='')
        if v % 2 == 0:
            cont1 += v
        cont += 1
        if cont > 6:
            cont2 += v
        if 3 < cont < 7:
            if cont == 4:
                cont3 = v
            if cont3 <= v:
                cont3 = v
print(f'-=-' * 20)
print(f'A soma de todos os valores pares é: {cont1}')
print(f'A soma da terceira coluna é: {cont2}')
print(f'O maior valor da segunda linha é: {cont3}')


