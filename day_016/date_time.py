from datetime import datetime, date, time, timedelta
#1
now = datetime.now()
print(now)
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
timestamp = now.timestamp()

#2
d = now.strftime("%m/%d/%Y, %H:%M:%S")
print(d)

#3
