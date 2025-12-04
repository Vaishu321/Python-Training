
items = {"item1": 50, "item2": 150, "item3": 200}
filtered = {}

for key, value in items.items():
    if value >= 100:
        filtered[key] = value

print(filtered)  # {'item2': 150, 'item3': 200}
