from datetime import datetime, date,time,timedelta

start_date= date(2024,1,1)
end_date= date(2024,12,31)
count=0
while start_date<=end_date:
    l=["Monday","Tuesday","Wednesday","Thursday","Friday"]
    if start_date.strftime("%A") in l:
        count += 1
    start_date=start_date+timedelta(days=1)



print("No. of weekdays: ",count)


