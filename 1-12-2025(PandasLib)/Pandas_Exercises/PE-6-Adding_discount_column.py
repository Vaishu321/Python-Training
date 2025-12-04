import pandas as pd
df=pd.read_csv("retail_sales.csv")

df["Discount"]=df.apply(lambda row: row["TotalPrice"]*0.9 if row["CustomerType"]=="Returning" else row["TotalPrice"]*0.95,axis=1)
print(df)
