# -*- coding: utf-8 -*-
"""
Created on Tue May 16 22:07:56 2023

@author: Alunc
"""

class triangulo:
    def __init__(self, lado1, lado2, lado3, base, altura):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def tipo(self):
        if self.lado1 > self.lado2 + self.lado3:
            return 'não é um triangulo !'
        elif self.lado1 == self.lado2 or self.lado1==self.lado3 or self.lado1 == self.lado2:
            return 'Triangulo insóceles'
        else:
            return 'outro tipo de triangulo'



t1 = triangulo(2, 1, 3, 4, 3)
t2= triangulo(8, 8, 8, 16, 9)

print(t1.tipo())
print(t2.tipo())


