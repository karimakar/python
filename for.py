# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 01:29:52 2023

@author: KARIM
"""
#     for loop
# for list
my_lst = ['karim','jo','adams','jena','kamard']

for j in my_lst:
    print(j)
#  for dictionnaire 
    print('*' *78)
dicto = {'a':1,'b':2,'c':3,'d':4,'e':5} 
for i in dicto.keys():
    print(i)
print('*'*75)    
for j in dicto.values():
    print(j)    
# using items
print('/' * 78)
for i,j in dicto.items():
    print(i,j)    
    
# looping if string
print('/' * 78 )
for i in 'ouarzazate':
    print(i)    
    
# break statment if for loop
print('/' * 80)

for key in my_lst:
  print(key)    
  if key == 'adams':
      break
  
print('*' * 80)   
for i in my_lst:
   if i == 'adams':
       break
   print(i)
   
   
# ================================>continue statment 
print('/' * 81)
for j in my_lst:
    if j == 'jena':
        continue
    print(j)
    
# ===================================>range function 

print('*/' * 80)
for x in range(10):
     print(x) 
     
print('/' * 80)

for i in range(2,6):
    print(i) 


print('/' * 80)

for i in range(4,30,1):
     print(i)    
     
     
# =============================>else statment 


print('/'*50)     
for l in range(10):
      print(l)
else:
    print('we are done')
    
    
print('/' * 45)

for k in range(12):
      if k == 6:break
      print(k)
else:
    print('we are finished') 
    
# Nested loop

data = [1,2,3,4]
data1 = ['karim','test','krsih','sow']

for i in data:
    for j in data1:
        print(i,j)
        
# pass statment

for k in data:
    pass        