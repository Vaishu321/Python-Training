import pandas as pd

df=pd.read_csv("superstore.csv")

filtered_df=df[(df["Returned"]=="Yes")]
print(filtered_df)