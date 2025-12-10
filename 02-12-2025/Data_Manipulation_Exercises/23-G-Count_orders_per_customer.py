import pandas as pd

df=pd.read_csv("superstore.csv")

grouped_df=df.groupby("CustomerName")["OrderID"].count()
print(grouped_df)