import pandas as pd

df = pd.read_csv("superstore.csv")
df["OrderDate"] = pd.to_datetime(df["OrderDate"])  #
df["OrderDate"] = df["OrderDate"].dt.month

pivot_profit = df.pivot_table(index='OrderDate', columns='Region', values='Quantity', aggfunc='sum')
print(pivot_profit)