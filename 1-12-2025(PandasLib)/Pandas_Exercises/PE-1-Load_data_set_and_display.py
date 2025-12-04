import pandas as pd

f=pd.read_csv('retail_sales.csv')
df=pd.DataFrame(f)

print(df.head(5))
print(df.tail(5))
print(df.columns)
print(df.shape)
