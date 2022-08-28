from uteis import numeros

print('-=-=-=-=-=CÁLCULO DO FATORIAL=-=-=-=-=-=-=')
num = int(input('Digite um número: '))
fat = numeros.fatorial(num)
print(f'O fatorial do número {num} é {fat}')
print(f'O dobro do número {num} é {numeros.dobro(num)}')
print(f'O triplo do número {num} é {numeros.triplo(num)}')
