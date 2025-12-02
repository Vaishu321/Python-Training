import pandas as pd

df=pd.read_csv("superstore.csv")

grouped_df=df.groupby("SubCategory")["Quantity"].sum()
print(grouped_df)