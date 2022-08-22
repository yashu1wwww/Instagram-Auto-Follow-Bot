import datetime as dt


now = dt.datetime.now()

print(now)

year = now.year
month = now.month
day = now.day
hour = now.hour
weekday = now.weekday()
print(year, month, day, hour, weekday)

print(type(now))
print(type(year))


# create new datetime object
dob = dt.datetime(year=1999, month=7, day=15)
print(dob)
