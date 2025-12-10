import pandas as pd

df = pd.read_csv("superstore.csv")

pivot_profit = df.pivot_table(index='ProductName', columns='Category', values='UnitPrice', aggfunc='mean')
print(pivot_profit)