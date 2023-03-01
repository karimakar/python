# -*- coding: utf-8 -*-
"""
Created on Wed Mar  1 19:04:46 2023

@author: PC-KARIM
"""

# cheking the data type 

import numpy as np

arr = np.array([12,3,4,8])
print('show array',arr)
print('/*' * 30)
print(arr.dtype)

arr = np.array(['ouarzazate','makkarkech','rabat'])

print(arr.dtype)

# create our array with special dtype

arr = np.array([1,2,3,4],dtype='S')

print('*' * 30)
print(arr)
print(arr.dtype)
print('*' * 25)
arr = np.array([1,2,3,4],dtype='i4')
print(arr)
print(arr.dtype)

print('*'*30)

arr =np.array(["a",1,2],dtype='S')

print(arr)

# use astype

arr = np.array([1.1,2.5,4.3])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

# use int
print('*'*20)
arr = np.array([1.1,2.5,4.3])
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

# =======================================================

print('*'*20)

arr = np.array([32,45,66])

newarr = arr.astype(bool)

print(newarr)

print(arr.dtype)

#==========================Diff between copy and view==========

arr = np.array([1,2,3,4,5,6,7])

x= arr.copy()
arr[0]=9

print('values of arr:',arr)
print('values of x:',x)


#              ==============view
print('*'*30)
arr = np.array([1,2,3,4,5,6,7])

x= arr.view()
arr[0]=9

print('values of arr:',arr)
print('values of x:',x)

# make change the view

x[1]=10

print(x)
print(arr)


# ckeck own data of array

arr = np.array([1,2,3,4,5,6,7])

x= arr.copy()
y = arr.view()

print('x',x.base)
print('y',y.base)


# shape
print('*'*25)
ar = np.array([[1,2,3,4,5],[8,9,7,3,4]])
print(ar.shape)

arr = np.array([1,2,5,4,7],ndmin=5)

print('shape of array is:',arr.shape)

#  use reshape================= 1D to 2D 

arr = np.array([1,2,5,6,4,7,8,9,2,10,11,12])

print(arr)
print(arr.shape)
print('new shape is:')
arr1 = arr.reshape(3,4)


print(arr1.ndim)

#  1D TO 3D
arr3 = arr.reshape(2,3,2)
print(arr.reshape(2,3,2))
print(arr3.ndim)

# unkown dimension

newarr = arr.reshape(2,2,-1)

print(newarr.ndim)

# =========================flattening arrays

arr = np.array([[1,2,3],[6,7,8]])

newar = arr.reshape(-1)
print(newar)
print(newar.ndim)

# iterating in array
print('*'*8)
arr = np.array([12,3,4,5,8])

for x in arr:
    print(x)
    
print('*'*20)    

ar = np.array([[1,2,3,4,5],[8,9,7,3,4]])

for i in ar:
    for j in i:
       print(j)  
       
# iterat in 3 dim

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    for y in x:
        for e in y:
            print(e)
       
# we can iterat using nditer
            
for i in np.nditer(arr): 
     print(i)

# join two arrays

arr1 =np.array([1,2,3])
arr2  = np.array([4,5,6])   
print('/'*20) 
arr = np.concatenate((arr1,arr2))
print(arr)      
            