import pandas as pd

df=pd.read_csv("superstore.csv")

lookup= pd.DataFrame({
    "Segment":["Consumer","Corporate","Home Office"],
    "Discount":[5,8,10]
})
merged=df.merge(lookup,how="left",on="Segment")
print(merged)