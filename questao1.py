#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @file	   	   : questao1.py

"""

"""
import numpy as np

np.random.seed(1)

# 1-) Crie um array aleatório de 15 itens entre 0 e 100
array = np.random.randint(0, 100, 15)
print('Array com 15 valores no intervalo [0, 100]')
print(array)

# 2-) Qual o maior número do array?
print('-' * 50)
print(f'Maximo: {array.max()}')

# 3-) Qual a sua posição?
print('-' * 50)
print(f'Posicao maximo: {array.argmax()}')

# 4-) Quais números do array são maiores que 10?
print('-' * 50)
print('Numeros > 10')
bigger_than_10 = array[array > 10]
print(f'{bigger_than_10}')

# 5-) Crie um novo array em que existam apenas elementos entre 10 e 30 (10 e 30
# inclusos)
print('-' * 50)
new_array = array[(array >= 10) & (array <= 30)]
print('Array com valores no intervalo [10, 30]')
print(f'{new_array}')
