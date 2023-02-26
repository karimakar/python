# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 01:08:16 2023

@author: KARIM
"""

#                           while loop
# basic syntax of while loop

i = 1
while i<10:
    print(i)
    i+=1
    
# ==============================>break statment

j = 1
while j<12:
    print(j)
    if j == 7:
        break
    j=j+1
#=============================> contiune statment
print('*' * 45)
k = 0
while k<12:
   
   k = k+1
   if k == 6:
       continue
   print(k)
    
# =========================> else statment

print('*' * 50)
i = 0
while i<=6:
    print(i)
    i = i+1
else:
    print('i is less than or equal  6')
    