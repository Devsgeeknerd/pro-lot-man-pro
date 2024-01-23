from random import randint
from time import sleep

# Lista temporária para armazenar números sorteados.
lista = list()

# Lista para armazenar os bilhetes gerados.
jogos = list()

# Mensagem visual.
print('-' * 30)
print('         LOTO MANIA         ')
print('-' * 30)

# Solicita ao usuário a quantidade de bilhetes desejada.
quantidade = int(input('Quantos bilhetes quer gerar? '))
total = 1

# Loop principal para gerar os bilhetes.
while total <= quantidade:
    # Inicializa a contagem de números únicos para cada bilhete.
    contagem = 0
    
    # Loop interno para gerar 50 números únicos para cada bilhete.
    while True:
        # Gera um número aleatório entre 1 e 100.
        numero = randint(1, 100)
        
        # Verifica se o número já foi sorteado.
        if numero not in lista:
            # Adiciona o número à lista temporária.
            lista.append(numero)
            
            # Incrementa a contagem de números únicos.
            contagem += 1
        
        # Se atingiu 50 números únicos, sai do loop interno.
        if contagem >= 50:
            break
    
    # Ordena a lista temporária em ordem crescente.
    lista.sort()
    
    # Adiciona uma cópia da lista temporária à lista de bilhetes.
    jogos.append(lista[:])
    
    # Limpa a lista temporária para o próximo bilhete.
    lista.clear()
    
    # Incrementa o total de bilhetes gerados.
    total += 1

# Mensagem indicando que os bilhetes estão sendo sorteados.
print('-=' * 6, f' SORTEANDO OS {quantidade} JOGOS ', '-=' * 6)

# Imprime cada bilhete numerado com pausa de 1 segundo entre cada impressão.
for i, l in enumerate(jogos):
    print(f'Bilhete {i + 1}: {l}')
    sleep(1)

# Mensagem desejando boa sorte.
print('-=' * 9, '< BOA SORTE!!! >', '-=' * 9)
