''' 
Entrada -> uma sentença do tipo " 19 + 5 ", separar essa string e filtrar a operacao dela
Saida -> printar o valor calculado
'''
import os

def soma(a, b):
    return a+b
    
def sub(a, b):
    return a-b

def mult(a, b):
    return a*b

def div(a, b):
    return a/b

sentenca = input('Entre com a sentenca separada por espaco: ').split(' ') # 19 + 5

try:
    s1 = int(sentenca[0])
    s2 = int(sentenca[2])
except:
    print('Somente numeros e a operacao')
    os.abort()

if sentenca[1] == '+':
    print( soma(s1, s2) )

elif sentenca[1] == '-':
    print(sub(s1, s2))

elif sentenca[1] == '*':
    print(mult(s1, s2))

elif sentenca[1] == '/':
    print(div(s1, s2))

else:
    print('digita um operador logico direito seu porra')