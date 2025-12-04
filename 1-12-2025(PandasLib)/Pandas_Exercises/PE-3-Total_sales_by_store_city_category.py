import pandas as pd

df=pd.read_csv('retail_sales.csv')

Total_sales=df.groupby("Store")["TotalPrice"].sum()
print("Total Sales by store: ",Total_sales)

Total_sales1=df.groupby("City")["TotalPrice"].sum()
print("Total Sales by city: ",Total_sales1)

Total_sales2=df.groupby("Category")["TotalPrice"].sum()
print("Total Sales by category: ",Total_sales2)
