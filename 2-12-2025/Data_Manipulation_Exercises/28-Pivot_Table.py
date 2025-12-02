import pandas as pd

df = pd.read_csv("superstore.csv")

pivot_profit = df.pivot_table(index='SubCategory', columns='Segment', values='Profit', aggfunc='sum')
print(pivot_profit)