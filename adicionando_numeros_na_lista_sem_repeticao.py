lista = list()
while True:
    ll = int(input('Digite o número desejado: '))
    if ll not in lista:
        lista.append(ll)
        print('Adicionado com sucesso...')
    else:
        print('Número já possui na lista!')
    n = str(input('Quer continuar [S/N]'))
    if n in 'Nn':
        break
lista.sort()
print(f'Você digitou os valores {lista}')