'''
@autor Everton Gomes

Crie um programa que receba um número inteiro não-negativo de segundos e converta-o em horas,
minutos e segundos. Exemplo: 3665 segundos correspondem a 1 hora, 1 min e 5 segundos.
Para tanto utilize os operadores “/” e “%”.
'''

a = int(input('digite o segundo')) * -1

hora = int(a / 3600)
minutos = int((a - (hora * 3600)) / 60)
segundos = int(a % 60)

print(hora,'hora(s)',minutos,'minutos(s)',segundos,'segundo(s)')
