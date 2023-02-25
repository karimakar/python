# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 19:52:02 2023

@author: KARIM
"""

#  ===========================> Python Conditions and If statements 

a = 30
b = 40
if b>a:
    print('b is greater than a')
    
    
# identation

c = 100
d = 300 
if c<d :
   print('c is less than d')    
   
#  ilif expression
   
a = 30
v = 300
if a<v :
    print('v is greater than a')
elif a == v:
    print('a equl to v')
    
    
# else keyword

a = int(input('give me some value for a'))
b = int(input('give me some value for b'))
if a<b :
   print('a is less than b')    
   
elif a== b:
    print('a is equal to b')
    
else:
    print('a is greater than b')   
    
    
    
# we can use just else if secanrios is limited

j = 30
n = 40

if j<n :
    print('j is less than n')  
else  :
     print('j is greater the n')    
     
     
     
 #=============================> short hand if
     
if j<n : print("j is small")     

a = 12
b = 14
# ============================> short hand if ...else
print('a < b') if a < b  else print('a>b')


def maxi(a,b):
    if a<b:
        print('a is less than b')
    else:
        print('a is greater than b')
        
maxi(14,57)        



# ========================>short hand with 3 condtions

print('B') if a<b else  print('==') if a == b else print('A')


# =======================>use 3 varibales using and close

a = 130
b = 120
c = 200

if a > b and c > a :
    print('c is the big number')
# or keyword    
if a > b or c > a :
    print('a is the big number')
    
    
#===================================> Not
    
a = 11
b = 10
if not a<b:
    print('a is greater than b')    
    
    
 #=================================>   Nested if
    
x = 9
        
    
if x > 10:
   print(' x is greater than 10')
   if x > 20 :
       print('x is also greater than 20')
       if x>30 :
           print('x also greater than 30')
   else:
       print('x is small not above ')
       
else :
 print('this number is out range')  


# =========================================>pass key word
 
 d = 100
 b = 147
 if d>b :
     pass 

     
    