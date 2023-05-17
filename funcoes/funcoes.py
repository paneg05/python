# -*- coding: utf-8 -*-
"""
Created on Tue May 16 20:07:17 2023

@author: Alunc
"""

def mensagem(texto):
    print(texto)


mensagem('parametro da função')


def soma(a,b):
    print(a+b)

soma(1,2)

def soma1(a,b):
    return a+b

print(soma1(1,2))


def calculaEnergiaPotencialGravitacional(m, h, g = 9.8):
    e = g*m*h
    return e

print(calculaEnergiaPotencialGravitacional(30, 12))
