import pandas as pd

df = pd.read_csv("superstore.csv")

pivot_profit = df.pivot_table(index='Region', columns='Returned', values='OrderID', aggfunc='count')
print(pivot_profit)