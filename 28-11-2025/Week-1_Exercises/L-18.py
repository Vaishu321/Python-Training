
people = [
    {"name": "Asha", "age": 30},
    {"name": "Bala", "age": 25},
    {"name": "Chitra", "age": 28},
]

people_sorted = sorted(people, key=lambda p: p["age"])
print(people_sorted)
