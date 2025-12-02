import pandas as pd

df = pd.read_csv("superstore.csv")

df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["Year"] = df["OrderDate"].dt.year
df["Month"] = df["OrderDate"].dt.month
df["Day"] = df["OrderDate"].dt.day
print(df.head())