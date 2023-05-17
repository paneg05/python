# -*- coding: utf-8 -*-
"""
Created on Tue May 16 19:12:27 2023

@author: Alunc
"""

#tuplas

tupla = ('cabra','doguinho','gato')
print(tupla[0])
print(tupla.index('cabra'))

for el in tupla:
    print(el)

#listas
lista1 =['oreia','manga','melancia']
lista2 = ['sorvete','arroz doce',' abacate']

l3 = lista1 + lista2
print(l3)

l2_2 = lista2 * 2
print(l2_2)

lista1.append('adicionando')
print(lista1)

lista1.remove('adicionando')
print(lista1)

del(l3)

#dicionarios    ? JSON ?
coleta = {
        'aedes aegypt' : 32,
        'aedes albopictus' : 22,
        'anopheles darlingi' : 14
    }

print(coleta['aedes aegypt'])

del(coleta)['aedes aegypt']
print(coleta)
print(coleta.items())
print(coleta.keys())
print(coleta.values())

for especie, numEspeciemes in coleta.items():
    print(f'especie: {especie}, número:{numEspeciemes}')
    
    
#conjuntos  

biomoleculas = ('proteinas','ácidos núcleicos','carboidratos','lipídeos','ácidos núcleicos')


print(set(biomoleculas))


c1 = {1,2,3,4,5}
c2 = {3,4,5,6,7}

c3 = c1.intersection(c2)

print(c3)

print(c1.difference(c2))
print(c2.difference(c1))
































