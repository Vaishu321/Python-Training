import pandas as pd
df=pd.read_csv('retail_sales.csv')

sorted_df=df.sort_values("TotalPrice", ascending=False)
print(sorted_df.head(5))
