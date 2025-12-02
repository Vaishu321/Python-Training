import pandas as pd

df=pd.read_csv("superstore.csv")



df["OrderDate"]=pd.to_datetime(df["OrderDate"])
df["ShipDate"]=pd.to_datetime(df["ShipDate"])
df["ShippingDays"]=df["ShipDate"]-df["OrderDate"]

grouped_df=df.groupby("Category")["ShippingDays"].mean()
print(grouped_df)