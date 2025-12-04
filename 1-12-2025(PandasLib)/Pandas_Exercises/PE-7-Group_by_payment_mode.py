import pandas as pd

df=pd.read_csv("retail_sales.csv")

pay_count=df.groupby("PaymentMethod")["OrderID"].count() #To calculate no. of orders grouped by orderID
print(pay_count)
