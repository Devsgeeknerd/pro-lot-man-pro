# Importação de bibliotecas
from random import randint
from time import sleep

lista = list()
""" Criação de uma lista vazia """

jogos = list()
""" Criação de uma lista vazia """

# Título do Programa
print('-' * 30)
print('         LOTOMANIA         ')
print('-' * 30)

# Pede para o usuário informar o numero de jogos.
quantidade = int(input('Quantos bilhetes quer gerar? '))
total = 1

# Loop para gerar os jogos.
while total <= quantidade:
    """ Criação de uma lista vazia. """
    contagem = 0
    while True:
        numero = randint(1, 100)
        if numero not in lista:
            lista.append(numero)
            """ Adiciona o numero na lista. """
            contagem += 1
            """ Conta quantos números foram adicionados. """
        if contagem >= 50:
            """ Verifica se o número de números adicionados é igual a 50. """
            break
            """ Sai do loop. """
    lista.sort()
    """ Ordena a lista. """
