valores = []
for c in range(0, 6):
    n = int(input(f'Dígite o {c}º valor: '))
    if len(valores) == 0:
        valores.insert(0, n)
    if n > max(valores):
        l = max(valores)
        l1 = valores.index(l)
        valores.insert(l1+1, n)
    p = 0
    while p < len(valores):
        if n < valores[p]:
            valores.insert(p, n)
            break
        p += 1
print(valores)

