# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 02:14:03 2023

@author: KARIM
"""
# create parent class 

class Person:
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    def inf(self):
        print('your full name is:',self.first_name,self.last_name)
        print('your age is:',self.age)
        
p = Person('karim','akarkab',30)
p.inf()

# create child class
print('*'*45)
class Student(Person) :
       def __init__(self,first_name,last_name,age):
           Person.__init__(self,first_name,last_name,age)
          
stu = Student("ali",'khan',49)
stu.inf() 
print('*'*45)
class Student(Person) :
       def __init__(self,first_name,last_name,age,level):
          super().__init__(first_name,last_name,age)  
          self.level = 'bac'
stu1 = Student('karim','akakka',30,'bac')
stu1.inf()
print(stu1.level)


# create class Employee

class Employee(Person):
    def __init__(self,first_name,last_name,age,salary,promotion):
        super().__init__(first_name,last_name,age)
        self.salary = salary
        self.promotion = self.salary * 0.2
    def sal(self):
        print('your salary is',self.salary)
        print('promotion is',self.promotion)
    def pro(self):
        print('after promotion you have stat of manager')
        
e = Employee('kraim', 'akaekb',30 ,15000,0)  
e.inf()      
e.sal()
e.pro()



