import pandas as pd

df=pd.read_csv("superstore.csv")
df["ShipDate"]=pd.to_datetime(df["ShipDate"])
filtered_df=df[(df["Category"]=="Furniture")&(df["ShipDate"]>"2024-01-20")]
print(filtered_df[["Category","ShipDate"]])