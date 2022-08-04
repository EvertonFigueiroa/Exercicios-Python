listap = list()
list1 = list()
list2 = list()
for c in range(1, 8):
    n = int(input(f'Digite o {c} número: '))
    if n % 2 == 0:
        list1.append(n)
    else:
        list2.append(n)
#list1.sort()
#list2.sort()
listap.append(list1)
listap.append(list2)
listap.sort()
print(f'Os valores pares são: {listap[0]}')
print(f'Os valores ímpares são: {listap[1]}')
