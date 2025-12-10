import pandas as pd

df=pd.read_csv("superstore.csv")

filtered_df=df[(df["Category"]=="Technology") & (df["Sales"]>400)]
print(filtered_df)