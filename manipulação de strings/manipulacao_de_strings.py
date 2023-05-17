# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

numero = 3
palavra =  'aass'
print(palavra.lower())

print(palavra.upper())

print(palavra.capitalize())

metadePalavra = palavra[0:2]
print(metadePalavra)


ultimasLetras = palavra[3:]
print(ultimasLetras)

b = palavra.replace('ss', 'new')
print(b)

indexOf= b.find('n')
print(indexOf)

length = len(palavra)
print(length)

trim = palavra.strip()
print(trim)

n1 = 30
n2 = 40

print(f'dividindo {n1} por {n2} o resultado é {n1 / n2}')
