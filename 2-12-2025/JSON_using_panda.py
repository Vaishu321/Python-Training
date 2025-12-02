import pandas as pd

#Create a DataFrame
df= pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Mary"],
    "Marks": [85,92, 78, 62],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore"]
})

#Write to JSON file
df.to_json("students.json", orient="records", indent=4)

print("JSON file created")

#Read the same JSON file
df=pd.read_json("students.json")

print("JSON file read successfully")
print(df)