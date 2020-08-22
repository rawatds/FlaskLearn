from datetime import datetime
import  pytz
from dateutil.tz import tzlocal
from dateutil import parser

format = "%Y-%m-%d %H:%M:%S %Z%z"
# Current time in UTC
now_utc = datetime.now()
print("now_utc:\n", now_utc, sep='')
now_utc = now_utc.astimezone(pytz.timezone('UTC'))
print(now_utc, sep='')
print(now_utc.strftime(format))


# Convert to Asia/Kolkata time zone
now_asia = now_utc.astimezone(pytz.timezone('Asia/Kolkata'))
print(now_asia.strftime(format))

now_ist = now_utc.astimezone()

print(now_utc)
print(now_asia)
print(now_ist)


#a = datetime.utcfromtimestamp('2020-08-22 08:56:49.539342')
a = '2020-08-22 08:56:49.539342'
#a= "2020-08-22 17:27:04.268393"
f = '%Y-%m-%d %H:%M:%S.%f'
b = datetime.strptime(a, f)
print("b:", b, type(b))

c = b.replace(tzinfo=pytz.UTC)
print("c:" , c, type(c))
d = c.astimezone(tzlocal())
print("d:",d)

# ----------------------------

#utc = datetime.datetime.utcnow() # Wrong - no TZ info here.

#utc = datetime.datetime.now(tz=pytz.timezone('UTC'))
#print("utc:", utc)

#ist_with_tz = utc.astimezone(tzlocal())
# OR
# ist_with_tz = utc.astimezone().isoformat()

#print("ist:", ist_with_tz)




#print((ist_with_tz - ist_with_tz.utcoffset()).replace(tzinfo=pytz.UTC))

# UTC_datetime = datetime.datetime.utcnow()
# print(UTC_datetime)
# UTC_datetime_timestamp = float(UTC_datetime.strftime("%c"))
# print(UTC_datetime_timestamp)
# local_datetime_converted = datetime.datetime.fromtimestamp(UTC_datetime_timestamp)
# print(local_datetime_converted)



# ist_current_time =
# print(ist_current_time.time())
# print(ist_current_time.strftime('%d %b, %Y at %H:%M'))
