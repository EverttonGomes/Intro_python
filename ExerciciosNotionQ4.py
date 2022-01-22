'''
@autor Everton Gomes

Um ano bissexto é um ano que é divisível por 4 mas não por 100 a não ser que seja divisível por 400.
Escreva um programa que leia um ano e imprima uma mensagem na tela dizendo se o mesmo é bissexto ou não.
'''

ano = int(input('digite um ano'))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(ano, 'ano bissexto')
else:
    print(ano, 'não é ano bissexto')