import pandas as pd

# For 1D we use Series
s=pd.Series([10,20,30])
print(s)

#For 2D we use DataFrame
data = {
    "Name":["Aisha","Rahul","John"],
    "Marks":[85,92,78]
}

df=pd.DataFrame(data)
print(df)