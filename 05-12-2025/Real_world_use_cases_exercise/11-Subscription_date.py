from datetime import datetime,date,time,timedelta

start_date= date.today()

subscription_days=int(input("Enter subscription days: "))

end_date= start_date + timedelta(days=subscription_days)

print("The subscription expiry date is:",end_date)