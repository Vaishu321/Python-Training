import pandas as pd

df=pd.read_csv("superstore.csv")

filtered_df=df[(df["Profit"]<20)]
print(filtered_df[["ProductName","Profit"]])