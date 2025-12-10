import pandas as pd

df=pd.read_csv("superstore.csv")

lookup= pd.DataFrame({
    "Region":["East","South","Central","West"],
    "Tax":[5,8,10,14]
})
merged=df.merge(lookup,how="left",on="Region")
print(merged)