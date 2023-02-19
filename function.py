# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 00:24:49 2023

@author: PC-KARIM
"""
# build function

def name():
    print('body of function')
    
name() 

# create add function
def add_num(x,y,z):
    a=x+y
    b=x+z
    c=y+z
    print(a,b,c)
    
# apply add_num function
add_num(1,2,3)    

# create prodcut_inf function

def product_info(product_name,price):
    print('Name of prodcut:',product_name)
    print("Price",price)
    
product_info('t-sihert', 15)   


product_info(product_name="jeans",price=120)

# return key word

def prod(a,b):
    return a*b

res = prod(4,5)
print('the result:',res)

#♠*********************************************
print('the result:',prod(4,5))
#example of buit it function 

ages = [5,12,17,18,24,32]
# *********************************************************
number = int(input('enter your number'))
def myfun(x):
    if x<number: 
        return False
    else:
        return True

adlut = filter(myfun,ages)

for x in adlut:
    print(x)

