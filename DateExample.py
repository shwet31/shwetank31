from datetime import datetime
delta = datetime.now()-datetime(1993, 10, 31)
print(delta.days)
print(delta.seconds)
print(delta.min)
print(type(delta))


#
date = datetime.now()
print('date', date)
then = datetime(1993, 10, 31, 11, 32, 00)  # year,month,date,hours,mins,seconds,microseconds
print('then', then)

# parsing date using string
whenever = datetime.strptime("1993-10-31,11:32:1", "%Y-%m-%d,%H:%M:%S")
print('whenever', whenever)

# returning date as a string
x = whenever.strftime("%d/%m/%Y")
print(type(x))
print(x)
