import pandas as pd

df = pd.DataFrame({
    "Name": ["Aisha", "Rahul", "John", "Neha", "Imran"],
    "Marks": [85, 92, 78, 65, 55],
    "City": ["Mumbai", "Delhi", "Chennai", "Bangalore", "Hyderabad"],
    "Age": [22, 25, 23, 21, 24]
})

df2 = df.copy()
df2.loc[2,"City"]= None #Creating a missing value
print(df2)
print(df2.isnull().sum()) #Sum is to add the total no. of null values in each column

df2_filled=df2.fillna("Unknown")
print(df2_filled)

#Fill NA fills all the None--0--Empty values ""--null values
#To unknown--Improves uniformity