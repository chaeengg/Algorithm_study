from datetime import datetime , timezone
from time import strptime

utc_time = datetime.utcnow()
utc_time1 = utc_time.strftime("%Y-%m-%d")

for i in range(3):
    print(utc_time1.split("-")[i])