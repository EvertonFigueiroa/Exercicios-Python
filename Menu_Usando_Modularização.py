from uteis.dados import *
from time import sleep
from uteis.arquivo import *

arq = 'registrodepessoas.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    sleep(1)
    anwers = menu()
    if anwers == 1:
        linhas()
        print('PESSOAS CADASTRADAS'.center(40))
        linhas()
        lerArquivo(arq)
    elif anwers == 2:
        linhas()
        print('NOVO CADASTRO'.center(40))
        linhas()
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrarArquivo(arq, nome, idade)
    elif anwers == 3:
        linhas()
        print('Saindo do sistema... Até logo!'.center(40))
        linhas()
        break
    else:
        print(f'\033[3;49;91mDígite uma opção valida!\033[m')
