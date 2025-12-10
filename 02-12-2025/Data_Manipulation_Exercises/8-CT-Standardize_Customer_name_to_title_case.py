import pandas as pd

df=pd.read_csv("superstore.csv")

df["CustomerName"]= df["CustomerName"].str.title()
print(df["CustomerName"])