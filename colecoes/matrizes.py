# -*- coding: utf-8 -*-
"""
Created on Tue May 16 19:49:08 2023

@author: Alunc
"""

import numpy as np

matriz = np.array([
            [1,2,3],
            [4,5,6]
        ]
    )

print(matriz)

print(matriz.shape)

print(matriz[0][1])

for i in range(matriz.shape[0]):
    print(matriz[i])
    for j in range(matriz.shape[1]):
        
        print(matriz[i][j])