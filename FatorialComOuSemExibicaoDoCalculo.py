def fatorial(n, show):
    f = 1
    for c in range(n, 0, -1):
        f *= c
    print(f)
    if show == True:
        f = 1
        for c in range(n, 0, -1):
            print(f'{c}', end='')
            if c == 1:
                print(f' = {f}')
            else:
                print(f' x ', end='')
            f *= c
    return f


question = int(input('Dígite um número: '))
answer = fatorial(question, show=True)


