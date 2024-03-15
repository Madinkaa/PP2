#Write a Python program to subtract five days from current date.
import datetime

x = datetime.datetime.now()
y = x - datetime.timedelta(days=5)

print(y)

#Write a Python program to print yesterday, today, tomorrow
import datetime

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)

print("Today: ", today)
print("Yesterday: ", yesterday)
print("Tomorrow: ", tomorrow)

#Write a Python program to drop microseconds from datetime
import datetime

x = datetime.datetime.now()
y = x.replace(microsecond=0)
print(y)

#Write a Python program to calculate two date difference in seconds
import datetime

x = datetime.datetime(2024, 3, 15)
y = datetime.datetime(2024, 3, 16)
z = (y - x).total_seconds()
print(z)