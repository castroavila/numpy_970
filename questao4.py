#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @file	   	   : questao4.py

"""

"""
import numpy as np

# Transforme o array em uma matriz 4 por 3 utilizando numpy.
arr = [
    1,
    2,
    3,
    4,
    'Amelia',
    'Bruna',
    'Carolina',
    'Débora',
    True,
    False,
    False,
    True,
]

# 4x3
new_array = np.array(arr).reshape(4, 3)
print('Array 4x3: ')
print(new_array)
print(f'shape: {new_array.shape}')

print('-' * 50)

# 3x4
new_array = np.array(arr).reshape(3, 4)
print('Array 3x4: ')
print(new_array)
print(f'shape: {new_array.shape}')
