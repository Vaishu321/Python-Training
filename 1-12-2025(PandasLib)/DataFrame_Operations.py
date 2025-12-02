import pandas as pd

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 23, 21, 24]
})

print(df)

print(df.head(2))
print(df.tail(2))

print(df.shape)
print(df.columns)
print(df.describe())