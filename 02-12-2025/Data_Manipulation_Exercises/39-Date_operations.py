# Find orders shipped in more than 5 days.
import pandas as pd

df = pd.read_csv("superstore.csv")
df["OrderDate"] = pd.to_datetime(df["OrderDate"])
df["ShipDate"] = pd.to_datetime(df["ShipDate"])

df["ShippingDays"] = df["ShipDate"] - df["OrderDate"]
print(df[(df["ShippingDays"] > '5 days')])