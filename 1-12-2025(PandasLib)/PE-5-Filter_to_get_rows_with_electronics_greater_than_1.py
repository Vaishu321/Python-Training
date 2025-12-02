import pandas as pd

df=pd.read_csv("retail_sales.csv")

filtered_df=df[(df["Category"]=="Electronics") & (df["Quantity"]>1)]
print(filtered_df)

