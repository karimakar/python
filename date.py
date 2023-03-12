
import datetime 
x = datetime.datetime.now()
print(x) 


# choose just year / month/day/hour/minute

print('year:',x.year)
print('month:',x.month)
print('day:',x.day)
print('hour:',x.hour)
print('minute:',x.minute)

# create datetime object
print('*' * 45)
y = datetime.datetime(2023,5,16)
print(y)
print(type(y))
print('*' * 45)
# use strftime function 
z = datetime.datetime(2023,6,23)
print(z.strftime('%B'))

print('short version weekday:')
print(z.strftime('%a'))
print('full version of weekday:')
print(z.strftime('%A'))

print('*'*44)
print('name of month:')
print(z.strftime('%b'))
print(z.strftime('%B'))
print('*'*45)
print('year:')
print(z.strftime('%y'))
print(z.strftime('%Y'))

print('*'*45)
print('Month')
print(z.strftime('%m'))

print('*'*44)
print('day of year')
print(z.strftime('%j'))

print('*'*44)
print('Centry')
print(z.strftime('%C'))

print('*'*44)
print('local version of time')
print(z.strftime('%x'))

print('*'*44)
print('loaal verion of time and date')
print(z.strftime('%c'))








