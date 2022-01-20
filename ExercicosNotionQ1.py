'''
@autor Everton Gomes

Um investidor possui um montante PV em dinheiro que deseja investir em uma aplicação
que rende uma taxa de i% por período (ex. um mês) em regime de juros compostos.
Sabendo que o valor FV ao final de “n” períodos é dado por: fv = pv * (1 + i/100) ** n
Escreva um programa que leia o valor PV a ser investido, a taxa de rendimento i, e a
duração do investimento (número de períodos n).
'''

fv = 0
pv = 200
i = 15
n = 5
for x in 0, n:
    fv = pv * (1 + i/100) ** n
print(fv)
