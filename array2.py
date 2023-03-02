# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 18:15:29 2023

@author: KARIM
"""
# joining arrays

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1,arr2))
print('*' * 45)
print('the result after concatination is:',arr)

print('*' *45)

print('we can also join arrays with 2 D')

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
arr = np.concatenate((arr1,arr2),axis=1)
print(('the result after conctatination of 2 D is:',arr))

print('/'*45)

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.stack((arr1,arr2),axis=1)
print('*' * 45)
print('the result after stack is:',arr)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
print('we use hstack function')
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.hstack((arr1,arr2))
print('*' * 45)
print('the result after hstack is:',arr)
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

print('we use hstack function')
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.vstack((arr1,arr2))
print('*' * 45)
print('the result after vstack is:',arr)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

print('we use hstack function')
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.dstack((arr1,arr2))
print('*' * 45)
print('the result after dstack is:',arr)
print('the dimension is:',arr.ndim)

#                          split arrays

print('*'*45)
print('we can split the arrays using array_split')

arr = np.array([1,5,8,9,7,6])
newarr = np.array_split(arr,3)
print('the newarry is:',newarr)

newarr1 = np.array_split(arr,4)
print('the newarry is:',newarr1)

print(newarr1[0])
print(newarr1[1])
print(newarr1[2])
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

print('we also split 2 D arrays')

arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
newarr = np.array_split(arr,3)
print('the new array is :',newarr)

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
print('*'*45)
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr,3)
newarr1 = np.array_split(arr,3,axis=1)

print('*'*40)
print('i can use hsplit')
newarr3 = np.hsplit(arr,3)



print('the result is:',newarr)
print('the result is:',newarr1)
print('the result is:',newarr3)

#♣    search in numpy

print('*'*40)
print('we can search in numpy using where')

arr = np.array([1,2,3,4,5,3,74,8,3])

y = np.where(arr==5)
c = np.where(arr%2==0)
print(c)
print(y)

#  searrchsort

arr = np.array([1,4,7,8,9])
x = np.searchsorted(arr, 7,side='left')
print('x:',x)

# sort functipn
print('/'*40)
print('use sort function')
arr = np.array([3,4,2,7,1])
print(np.sort(arr))

print('*'*40)

arr = np.array(['ouarzazzt','rabt','casa'])
print('string array',np.sort(arr))

print('*'*40)

arr = np.array([[3, 2, 4], [5, 0, 1]])
print('2D arrays',np.sort(arr))

# filter arrays

print('*'*40)

print('can filter in arrays')
arr = np.array([40,42,50,32,47,49,43])

# create empty array
filter_array =[]

for ele in arr:
    if ele > 42:
        filter_array.append(True)
    else:
        filter_array.append(False)
newarr = arr[filter_array]

print('filter_arr',filter_array)
print('newarr',newarr)

# =====================================================
print('/'*40)        

print('can filter in arrays')
arr = np.array([1,2,3,4,7,8,9,10,12,14,17,20])

# create empty array
filter_array =[]

for ele in arr:
    if ele %2 == 0:
        filter_array.append(True)
    else:
        filter_array.append(False)
newarr = arr[filter_array]
print('the element divide by 2 is')
print('filter_arr',filter_array)
print('newarr',newarr)







