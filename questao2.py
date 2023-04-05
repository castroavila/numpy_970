#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @file	   	   : questao2.py

"""

"""
import numpy as np

np.random.seed(1)

# 1-) Crie uma matriz (5, 2) com números igualmente espaçados entre 0 e 100
# (utilize o np.linspace)

array = np.linspace(0, 100, 10)
array = array.reshape(5, 2)
print(f'{array}')


# 2-) Qual o maior valor da matriz?
print('-' * 50)
print(f'Maximo: {array.max()}')

# 3-) Qual o valor máximo por linha?
print('-' * 50)
print('Maximo por linha')
print(f'{array.max(axis=1)}')

# 4-) Qual o valor máximo por coluna?
print('-' * 50)
print('Maximo por coluna')
print(f'{array.max(axis=0)}')


# 5-) Qual a média por linha?
print('-' * 50)
print('Media por linha')
print(f'{array.mean(axis=1)}')

# 6-) Qual a média da matriz?
print('-' * 50)
print('Media da matriz')
print(f'{array.mean()}')
