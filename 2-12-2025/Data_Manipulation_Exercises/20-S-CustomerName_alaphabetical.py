import pandas as pd

df=pd.read_csv("superstore.csv")

sorted_df=df.sort_values("CustomerName", ascending=True)
print(sorted_df["CustomerName"])