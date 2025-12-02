import pandas as pd

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 23, 21, 24]
})

#print(df)

#Transforming Data
df["Result"]=df["Marks"].apply(lambda x:"Pass" if x>70 else "Fail")
print(df)
#Sorting after transforming
sorted_df = df.sort_values(by="Marks", ascending=False)
print(sorted_df)