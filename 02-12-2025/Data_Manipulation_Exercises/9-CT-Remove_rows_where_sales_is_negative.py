import pandas as pd

df=pd.read_csv("superstore.csv")

df=df[df["Sales"]>0]

print(df["Sales"])