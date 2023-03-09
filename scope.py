# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 21:36:07 2023

@author: KARIM
"""
# scop in python

def my_function():
    y = 1500
    print(y)

# call my_function
    
my_function()

# function inside function

print('*' * 45)
def first_function():
    y = 100
    def secand_function():
        print(y)
    secand_function()
first_function()    

#♦ Global scop
print('*'*44)
t = 2000
def myfunction():
    print(t)
myfunction()
print(t)   

#                      Naming varibale
print('*'*45)
y = 1000
def test():
    y = 2000
    print(y)
test()
print(y)  

# global keyword
def test():
    global d
    d =100
test()
print(d)  


# we create the same varible with diffrent values
h = 400
def fonction():
    global h
    h=500
fonction()
print(h)    
    
