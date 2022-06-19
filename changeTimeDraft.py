import datetime
from dateutil import tz

#set variables to various time zones
can = tz.gettz('America/Montreal')
thai = tz.gettz('Asia/Bangkok')
madrid = tz.gettz('Europe/Madrid')
#create date time object in canadian time zone for future and now
x = datetime.datetime(2022,12,12,20,30).astimezone(can)
xx= datetime.datetime.now().astimezone(can)

#print output of datetime objects
print("future canadian time: " , x)
print("now canadian time" , xx)

#future time
thaiTimex = x.astimezone(thai)
madTimex = x.astimezone(madrid)
#currenttime in different zones
thaiTimexx = xx.astimezone(thai)
madTimexx = xx.astimezone(madrid)
#print outputs
print('later')
print(thaiTimex)
print(madTimex)

print("now")
print("thai", thaiTimexx)
print("madrid", madTimexx)


