import pandas as pd

df=pd.read_csv("superstore.csv")

df["ProfitMargin"]=df["Profit"]/df["Sales"]
print(df["ProfitMargin"])