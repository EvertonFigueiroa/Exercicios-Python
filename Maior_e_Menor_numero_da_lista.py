valores = list()
aa = list()
aa2 = list()
val = 0
val2 = 999
for c in range(0, 6):
    valores.append(int(input(f'Dígite o valor desejado na posição {c}: ')))
for v, c in enumerate(valores):
    if c >= val:
        val = c
    elif c <= val2:
        val2 = c
for v, c in enumerate(valores):
    if c == val:
        aa.append(v)
    elif c == val2:
        aa2.append(v)
print(f'Os valores digitados foram {valores}')
print(f'O maior número é {val} nas posições {aa}')
print(f'O menor número é {val2} nas posições {aa2}')



