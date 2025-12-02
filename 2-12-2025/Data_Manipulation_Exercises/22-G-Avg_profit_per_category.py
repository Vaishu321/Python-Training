import pandas as pd

df=pd.read_csv("superstore.csv")

grouped_df=df.groupby("Category")["Profit"].mean()
print(grouped_df)