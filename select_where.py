# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 00:44:18 2023

@author: PC-KARIM
"""

import mysql.connector

# create connection to database

mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='karim',
    password='0623963226',
    database='sales'
    
    )

#creare cursor
cur = mydb.cursor()

# create query
#query = str(input('enter myquery'))
sql1 = " select * from customers where custmer_name = 'Surge Stores'"
sql2 = "select * from customers"
sql3 = " select * from customers where custmer_name ='Excel Stores'"
sql4 = " select * from markets order by zone"
sql5 = "select * from transactions limit 100 "
cur.execute(sql5)
# store our result in res

res = cur.fetchall()

#resturn the results

for i in res:
   print(i)
    
print('*'*45)
