import pandas as pd

df=pd.read_csv("superstore.csv")

filtered_df=df[(df["Region"]=="West")]
print(filtered_df)