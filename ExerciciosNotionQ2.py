'''
@autor Everton Gomes

Escreva um programa que leia três números inteiros não-negativos representando as horas, minutos e segundos,
respectivamente e os converta em segundos. Exemplo: 2 h 40 min e 10 s correspondem a 9610 segundos.
'''

hora = int(input('Digite a hora'))
minutos = int(input('Digite os minutos'))
segundo = int(input('Digite os segundo'))

#1 hr = a 3600
saida = 'erro de sintaxe'
if hora >= 0:
    if minutos >= 0 and minutos < 60:
        if segundo >= 0 and segundo < 60:
            saida = (hora * 3600) + (minutos * 60) + segundo
print(saida)
