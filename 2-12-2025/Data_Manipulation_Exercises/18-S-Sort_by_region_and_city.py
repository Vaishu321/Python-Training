import pandas as pd

df=pd.read_csv("superstore.csv")

region_sorted_df=df.sort_values("Region", ascending=True)
print(region_sorted_df)

city_sorted_df=df.sort_values("City", ascending=True)
print(city_sorted_df)