# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 22:07:03 2023

@author: KARIM
"""

#    array

a = 10
b = 12
c = 100

car = ['fiat','dacia','bmw']
print(car[0])

car[1]='honda'
print(car)

#  array with numpy

import numpy as np

a = np.array((1,2,3))
print(a)
print(type(a))
        
#  create array

arr = np.array([1,2,3,4,5,6])

print(arr)

#╚  ==================================> 0 Dim array
print('*' * 45)

a = np.array(16)
print(a)
print("dimension of a:",a.ndim)
#  =====================================1-D arrays
print('*' * 45)
b = np.array([1,2,5,4,8,7,9])
print(b)
print("dimension of b:",b.ndim)
# =====================================2-D arrays

print('*' * 45)

c = np.array([[1,2,3,4],[5,6,7,8]])
print(c)
print("dimension of c:",c.ndim)
#======================================3- D arrays
print('*' * 45)

d = np.array([[[1,2,3],[7,8,9],[4,5,6]]])
print(d)
print("dimesnion of D:",d.ndim)

# create array with simpecific dim
print('*' * 45)

j = np.array([74,5,89,4,5],ndmin=5)

print("dimension is",j.ndim)

# acess arrays element
print('*' * 45)

print(arr[3])
print('*' * 45)

print('choose 2 d')

print(c[1][0])
print('*' * 45)

# choose element in 3 d
print(d[0][0][2])

# 
print('*' * 45)

print(arr[0] + arr[1])

# acess to element

print('choos two elements',c[0,1])

# sclicing array
arr = np.array([1,2,3,4,5,6,7,8,9])
print('*' * 45)

print(arr[1:6])
print(arr[2:])
print(arr[:6])
print(arr[-4:-1])
# step sclicing
print(arr[1:6:1])
print(arr[::2])





