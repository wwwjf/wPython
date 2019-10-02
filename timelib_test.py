import time
import datetime

print(time.time())
print(time.localtime())
print(time.strftime('%Y%m%d'))

print(datetime.datetime.now())
newTime = datetime.timedelta(minutes=10)
print(datetime.datetime.now() + newTime)
