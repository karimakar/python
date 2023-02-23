# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 00:24:49 2023

@author: KARIM
"""
# tuple
#==========================================>tuple

data = ('honda','dacia','pegeout','bmw')
print(data)

print(type(data))

#  allow dupliced

data1=('honda','dacia','pegeout','bmw','honda')
print(data1)

# lenght of tuple

print(len(data))
print(len(data1))

#             create tuple with one item

one = ('bmw',)
print(one)
print(type(one))

# we can create tuple with any data type
tuple1 = (1,2,3,5,4,8)
tuple2=( 'a','b','c','d')
tuple3 = (1.2,0.5,4.5,8.9)
tuple4 = ('with',1,9.3)
tuple5 = (True,False,True)
#  ------------------------------------
print(tuple5)

print(tuple4)
print(tuple2)
# --------------------------------------
a = tuple(('abc','bvd','fgh'))

print(a)
print(type(a))

# ========================================>Acess
print(data1)

print('the result of Frist index is:',data1[2])

# negative acsess *
print('the result is:')
print(data1[-1])

#<================================== Range of indexes
print('show me 2 items:',data1[1:3])
print('show some items:',data1[:4])
# =================================> Range of negative indexes
print(data1[-4:-1])
print('show some items:',data1[:-1])


# check extistance of an elemen:

print("*" * 60)
print(data)

if 'dacia' in data:
    print('yes,dacia is exist in store')
else:
    print('oops')    
    
print('*' * 80)    
print('change values')
#data[0]='fait'

b = list(data)
print(type(b))
b[0]='fiat'
print(b)
data = tuple(b)

print(data)

#                                Add items

f = list(data)
f.append('rolls')
print(f)
data = tuple(f)

print(type(data))

#                                remove tuple 

j = list(data)
j.remove('fiat')
print(j)

data = tuple(j)

# delete the tuple completly

del tuple2


#                               Unpackting tuple

data2 = ('blue','green','purple')

small,meduim,big = data2
print(small)

print(meduim)

print(big)

#                              use Asterisk

my_tuple = (1,2,5,7,8,9,6,1,4)

(a,b,*c) = my_tuple

print(a)

print(b)

print(c)


(f,*j,k) = my_tuple

print(f)

print(j)

print(k)

#•                               loops in tulpe=======


print(data1)

# for loop
for i in data1:
    print(i)
    
# while loop 
print('*' * 80)    
i =0
while i<len(data1):
    print(data1[i])
    i = i+1
#   join tuples
    
print(data)
print(data1)    

data3  = data + data1

print(data3)

data = data * 4
print(data)
    

# methods of tuple

print(data.count('bmw'))

x = data1.index(1)

print(x)