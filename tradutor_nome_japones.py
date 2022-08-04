def lin():
    print('-=-' * 20)


kanji = {'a': "ka", 'b': "tu", 'c': "mi", 'd': "te",
         'e': "ku", 'f': "lu", 'g': "ji", 'h': "ri",
         'i': "ki", 'j': "zu", 'k': "me", 'l': "ta",
         'm': "rin", 'n': "to", 'o': "mo", 'p': "no",
         'q': "ke", 'r': "shi", 's': "ari", 't': "chi",
         'u': "do", 'v': "ru", 'w': "mei", 'x': "na",
         'y': "fu", 'z': "zi"}
lin()
print(f'{"TRADUTOR DE NOME PARA JAPONÊS":.^60}')
lin()
while True:
    nomejp = ''
    nomebr = str(input('Digite seu nome: ')).strip().lower()
    for c in nomebr:
        nomejp += kanji[f'{c}']
    print(f'Seu nome japonês é {nomejp.title()}')
    lin()
    resp = str(input('Deseja continuar? [S/N] ')).strip().lower()
    if resp in 'n':
        break
    lin()

