# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 02:31:11 2023

@author: KARIM
"""
#=====================================Sets========================

data = {'lundi','mardi','jeudi','medrcedi'}
# show the sets
print(data)

print(type(data))

# data dulplicated not allowed

data1={1,2,3,1,1,5}

print(data1)

data2 = {'hi','hi','hi','hi'}
print(data2)

# with bool test

set_a = {1,2,3,5,True,False,0,'hello'}

print(set_a)

#               get the lengt of sets

print('the lenght of this set is:',len(set_a))

#   create set items Data Type

item1 = {1,2,3,4}
item2 = {'hi','hello','wolrd'}
item3 = {1.2,5.9,4.7,.0}
item4 = {True,False,True,False}

# create a set with constructor

my_set = set(('like','abmonne','test'))
print('type of my_set',type(my_set))

print('*' * 75)

#                   Acess to sets

for i in data:
    print(i)
    
print('*' *  70)    
# check if some value exist or not

print('jeudi' in data)  
print('vendredi' in data)  

# =======================================ADD========

data.add('dimanche')
print(data)

num1 = {1,2,3,4}
num2 = {5,6,7}
#                                    update
num1.update(num2)
print(num1)

lis= ['un','deux']

num1.update(lis)
print(num1)


# ===========================Revome=========================
# first method to delete values
data.remove('dimanche')

print(data)

#discard function

data.discard('mardi')

print(data)


# diff between discard and remove

# data.remove('mardi')

data.discard('dimanche')

# pop method

num1.pop()

print(num1.pop())
print(num1)

#     clear

num1.clear()

print(num1)


# for drop sets

del num1

#print(num1)


#   join two sets

a = {'a','b','c',4,6}
aa = {1,2,3,4,"a"}

set1 = a.union(aa)

print(set1)


# return only duplicted values
a.intersection_update(aa)

print('commun elements:',a)

e=a.intersection(aa)

print(e)


#  syemmtric_difference_update

aa.symmetric_difference_update(a)

print('diff elements:',aa)

a.symmetric_difference(aa)

print("symmetrict_diff",a)



#                  copy

semaine = data.copy()
  
print(semaine)

#             diffrence

a.difference(aa)
print(a)

#       isdijoint

a.isdisjoint(aa)

print(a)


# issubset

x = {"a",'b',"c","d","e","f"}
y={"b",'c',"j"}

z= x.issubset(y)

print(z)

l = x.issuperset(y)
print(l)

