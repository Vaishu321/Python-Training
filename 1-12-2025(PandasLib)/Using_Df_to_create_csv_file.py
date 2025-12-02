import pandas as pd

#Create Sample data
data={
    "Name":["John","Doe"],
    "Marks":[10,20],
    "City":["New York","Delhi"]
}

df=pd.DataFrame(data)

#Write CSV
df.to_csv("students.csv", index=False)
print("CSV file created")