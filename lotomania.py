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
    jogos.append(lista[:])
    """ Adiciona a lista na lista de jogos. """
    lista.clear()
    """ Limpa a lista. """
    total += 1
    """ Incrementa o total. """
print('-=' * 6, f' SORTEANDO OS {quantidade} JOGOS ', '-=' * 6)
""" Imprime o título. """
for i, l in enumerate(jogos):
    """ Imprime o número do jogo. """
    print(f'Jogo {i + 1}: {l}')
    sleep(1)
    """ Pausa de 1 segundo. """
