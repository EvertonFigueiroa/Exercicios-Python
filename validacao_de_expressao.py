l1 = list()
cont = 0
l1.append(str(input('Digite uma expressão: ')))
for c in l1:
    for i in c:
        if i == '(':
            cont += 1
        elif i == ')':
            cont += 1
if cont % 2 == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está invalida!')

