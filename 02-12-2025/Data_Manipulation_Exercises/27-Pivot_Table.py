import pandas as pd

df = pd.read_csv("superstore.csv")

pivot_sales = pd.pivot_table(df, index='Region', columns='Category', values='Sales', aggfunc='sum')
print(pivot_sales)