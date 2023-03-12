
try :
    print(y)
except:
    print('an excpetion occured')    

print('*'*44)
#print(z)

# ========================>  many excpetions
print('*'*45)
try:
    print(y)
except NameError:
    print('this variable is not defined')
except:
    print('Something well be wrong')    
    
# ================================> else
    print('*'*45)
try:
    print('hi world')
except :
    print('Someting well be worng')
else :
    print('Nothing well be wrong')    
    
# ===============================> finaly clause
print('*'*44)
i=0
try:
   print(i)
except:
   print('somethong be worng')
finally :
   print('the try except is finished')    
   
print('*'* 45) 
# function devision
def div(a,b):
    try:
        result = a//b
        print('your anser is:',result)
    except ZeroDivisionError:
        print('Sorry you are dividing by Zero')
        
div(5,0)  # =================> zerodivison
div(4,6)    # =================> 0

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
print('*'*45)
def ab(a,b):
    try:
        c = ((a+b)//(a-b))
    except ZeroDivisionError:
        print('a is equal to b')
    else:
        print(c)
ab(1.1,2.0)
ab(4.0,4.0) 

# finally clause
print('*'*45)
def division(a,b):
    try:
        v = a/b
    except ZeroDivisionError:
        print('avoid 0')
    else:
        print(v)
    finally:
        print('your operation is end')
        
division(4, 5) 
division(5,0)       
     