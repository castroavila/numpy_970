#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# @file	   	   : questao3.py

"""

"""
import numpy as np

# Imprima as dimensões (shape) dos seguintes arrays:

a = np.array(2)

b = np.array([1, 2, 3, 4, 5])

c = np.array([[1, 2, 3], [4, 5, 6]])

d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print('Array `a`:')
print(a)
print(f'shape: {a.shape}')
print('-' * 50)
print('Array `b`:')
print(b)
print(f'shape: {b.shape}')
print('-' * 50)
print('Array `c`:')
print(c)
print(f'shape: {c.shape}')
print('-' * 50)
print('Array `d`:')
print(d)
print(f'shape: {d.shape}')
