import pandas as pd

df=pd.read_csv("retail_50.csv")

#Queries

#Filtering
high_electronics=df[(df["Category"]=="Electronics") &(df["TotalPrice"]>10000)]
print(high_electronics)

#Sorting
sorted_df=df.sort_values("TotalPrice",ascending=False)
print(sorted_df)

#Grouping
#Sum of Total Price grouped by Category
category_sales=df.groupby("Category")["TotalPrice"].sum()
print(category_sales)
#Average off total price grouped by store
store_avg=df.groupby("Store")["TotalPrice"].mean()
print(store_avg)
#Orders grouped by City
city_orders = df.groupby("City")["OrderID"].count()
print(city_orders)