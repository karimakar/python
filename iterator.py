# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 19:21:39 2023

@author: KARIM
"""

# create u tuple of objects
my_tuple = ('ouarzazate','zgora','medlt')
my_iter = iter(my_tuple)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# create string value

test = 'manhatan'
my_test = iter(test)
print('*'*45)
# show all values of test
print(next(my_test))
print(next(my_test))
print(next(my_test))
print(next(my_test))
print(next(my_test))
print(next(my_test))
print(next(my_test))
print(next(my_test))

print('*'*45)
# we can looping this varible
for i in my_tuple:
    print(i)
print('loop for string value')    
print('*'*45)
# the same thing work with string
for x in test:
    print(x)  
print('*'*45)    
# create our iterator

class Mynumbers:
    def __iter__(self):
        self.k = 1
        return self
    def __next__(self):
        x= self.k
        self.k+=1
        return x
    
#create instance form this class
        
fi_class = Mynumbers()
my_iter = iter(fi_class)

print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# create the same class with stop iteration
print('/'*45)
class Mynumber :
    def __iter__(self):
        self.k = 1
        return self
    def __next__(self):
        if self.k<=30:
            x = self.k
            self.k+=1
            return x
        else:
            raise StopIteration
            
#create instance from this class

myclass=Mynumber()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))            
print(next(myiter))  
print(next(myiter))            
print(next(myiter))            
print(next(myiter))            
print(next(myiter)) 
print('*'*44)           
for i in myiter:
    print(i)
          
            
            