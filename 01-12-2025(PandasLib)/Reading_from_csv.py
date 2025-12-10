import pandas as pd

df=pd.read_csv('students.csv', index_col=0)

print("CSV File read successfully")
print(df)