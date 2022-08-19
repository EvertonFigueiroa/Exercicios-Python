def ficha(n="<desconhecido>", gol=0):
    print(f'O jogodar {n} fez {gol} gol(s) no campeonato.')


n1 = str(input('Nome do Jogador: '))
gols = str(input('Quantidade de Gols: '))

if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0

if n1.strip() == '':
    ficha(gol=gols)
else:
    ficha(n1, gols)


