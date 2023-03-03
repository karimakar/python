# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 00:36:27 2023

@author: KARIM
"""

# create class named test

class Test:
    y=10
    
# create objet

p = Test()    
print(p.y)

# create car class
print('*'* 45)
print('the init function in python blueprint objects')
class Car:
    def __init__(self,color,price):
          self.color = color
          self.price = price
    def __str__(self):
        return f"{self.color}({self.price})"
          
my_car1 = Car('red',100000)
print(my_car1.color)
print(my_car1.price) 
# create scand object
my_car2 = Car('blue',120000)
print('show the my_car2 object')
print(my_car2)         # ===> <__main__.Car object at 0x000002365836B148>
my_car3 = Car(color='green', price=50000) 
print(my_car3)   

class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def Age(self):
        print( 'my age is:',self.age)
    def Name(self):
        print('my name is:',self.name)
    def Gender(self):
        print('my gender is',self.gender)
        
 # create objets from  person class
print('*'*45)        
p1 = Person("karim",30,'Male')
p1.Age() 
p1.Gender()   
p1.Name()

print('*'*45)
p2 = Person('salma' ,20, gender='Female') 

p2.Name()
p2.Gender()
p2.Age()

#self parameter

class Cat:
    def __init__(abs,name,gender):
        abs.name = name
        abs.gender = gender
    def __str__(abs):
        return f'{abs.name}({abs.gender})'
cat1 = Cat(name='jo', gender='male')
print(cat1) 

# modifay object proprites
cat1.name='rex'
print(cat1)

del cat1.name
# del cat1

class MyTest:
    def __init__(self,price,pro):
        self.price = price
        self.pro = pro
    def tax(self):
        print(self.pro)
        print('the tax is',self.price * 0.2)
        
prod1 = MyTest(1500,'laptop')  
prod1.tax() 

class  peaple :
  pass    
        

        
        
        

