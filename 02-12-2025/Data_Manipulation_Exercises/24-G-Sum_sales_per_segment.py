import pandas as pd

df=pd.read_csv("superstore.csv")

grouped_df=df.groupby("Segment")["Sales"].sum()
print(grouped_df)