#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @file	   	   : questao5.py

"""

"""
import numpy as np

# Crie um array com 40 números aleatórios, distribuídos uniformemente, entre
# [0, 5).

# Para cada elemento do array, calcule:

#     Seno
#     Cosseno
#     Log na base 2
np.random.seed(1)
array = np.random.uniform(0, 5, 40)
print('Array: ')
print(array)
print('-' * 50)

# Assumindo que os elementos em `array` estão dados em graus, precisa-se
# converter deg to rad.
print('Seno')
print(np.sin(np.deg2rad(array)))

print('-' * 50)
print('Cosseno')
print(np.cos(np.deg2rad(array)))

print('-' * 50)
print('Log na base 2')
print(np.log2(array))
