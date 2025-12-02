import pandas as pd

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 23, 21, 24]
})

print(df)

print(df["Name"])
print(df[["Name","Marks"]])

#Filters

high_scores = df[df["Marks"] > 70]
print(high_scores)

filtered= df[(df["Marks"] > 70)&(df["Age"] >22)]
print(filtered)