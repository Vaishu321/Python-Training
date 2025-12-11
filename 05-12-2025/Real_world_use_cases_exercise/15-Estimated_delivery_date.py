from datetime import date, timedelta
order_date=date(2024,2,20)
days=int(input("Enter the number of days for delivery:"))
delivery_timeline=timedelta(days=days)

estimated_delivery_date=order_date+delivery_timeline
print("The estimated date of delivery is",estimated_delivery_date)