import datetime

print(datetime.datetime.now())
dt = datetime.datetime(2017, 5, 7, 16, 40, 20)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)
print(datetime.datetime.fromtimestamp(1494146655))