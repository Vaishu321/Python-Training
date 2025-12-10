import pandas as pd

df=pd.read_csv("superstore.csv")

sorted_df=df.sort_values("Sales", ascending=False)
print(sorted_df)