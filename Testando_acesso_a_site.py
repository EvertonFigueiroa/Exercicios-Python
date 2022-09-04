import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('\033[4;49;91m O site pudim não está acessível!\033[m')
else:
    print('\033[4;49;92m O site pudim está acessível!\033[m')

