print('-=-=-=-=-Quentinha do seu Carlos-=-=-=-=-')

almoco = {'Galinha': 0, 'Figado': 0, 'Guizado': 0}

valor = float(input('Quanto você deseja investir?: '))
valor1 = valor

print(f'Você consegue comprar um total de {valor // 12:.0f} Figados cada um por R$ 12,00')
print(f'Você consegue comprar um total de {valor // 9:.0f} Guizados cada um por R$ 9,00')
print(f'Você consegue comprar um total de {valor // 8:.0f} Galinhas cada um por R$ 8,00')

question = str(input('Você deseja escolher os pratos? [S/N]: '))

quantifig = 0
quantigal = 0
quantigui = 0
if question in 'Ss':
    quantifig = int(input('Quantos figados [0 para nenhum]: '))
    valor1 = valor1 - (quantifig * 12)
    print(f'Você ainda tem {valor1:.2f} reais para gastar!')
    if valor1 > 9:
        quantigui = int(input('Quantos guizados [0 para nenhum]: '))
        valor1 = valor1 - (quantigui * 9)
        print(f'Você ainda tem {valor1:.2f} reais para gastar!')
    if valor1 > 8:
        quantigal = int(input('Quantas galinhas [0 para nenhum]: '))
        valor1 = valor1 - (quantigal * 8)
        print(f'Você ainda tem {valor1:.2f} reais para gastar!')

if question in 'Nn':
    while True:
        if valor1 >= 12.00:
            valor1 -= 12.00
            almoco['Figado'] += 1
        if valor1 >= 9.00:
            valor1 -= 9.00
            almoco['Guizado'] += 1
        if valor1 >= 8.00:
            valor1 -= 8.00
            almoco['Galinha'] += 1
        else:
            print()
            print(
                f"Você vai conseguir comprar {almoco['Figado']} Figado(s), {almoco['Guizado']} Guizado(s) e {almoco['Galinha']} Galinha(s)!")
            print(f'O troco é de {valor1:.2f} reais')
            break

if question in 'Ss':
    total = (quantifig+quantigui+quantigal) * 14
    total2 = (quantifig + quantigui + quantigal) * 15
    lucros = total - valor
    lucroc = total2 - valor

    print()
    print(f"Você vai conseguir comprar {quantifig} Figado(s), {quantigui} Guizado(s) e {quantigal} Galinha(s)!")
    print(f'O troco é de {valor1:.2f} reais')

else:
    total = (almoco['Figado'] + almoco['Guizado'] + almoco['Galinha']) * 14
    total2 = (almoco['Figado'] + almoco['Guizado'] + almoco['Galinha']) * 15
    lucros = total - valor
    lucroc = total2 - valor
    print()
    print(
        f'O valor total investido foi de {valor:.2f} reais, com as vendas S/Cartão você recebeu {total:.2f} reais e lucro de {lucros:.2f} reais ')
    print(
        f'O valor total investido foi de {valor:.2f} reais, com as vendas C/Cartão você recebeu {total2:.2f} reais e lucro de {lucroc:.2f} reais ')
