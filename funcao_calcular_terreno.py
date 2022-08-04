def area(a, b):
    s = a * b
    print(f' A área do terreno {a}x{b} é de {s}m²')


print('    CALCULO DO TERRENO')
print('-=-' * 10)
area(float(input('Largura (m): ')), float(input('Comprimento (m): ')))
