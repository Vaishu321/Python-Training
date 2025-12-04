
employees = {
    "e1": {"dept": "IT"},
    "e2": {"dept": "HR"},
    "e3": {"dept": "IT"}
}

dept_count = {}

for emp in employees.values():
    dept = emp["dept"]
    if dept in dept_count:
        dept_count[dept] += 1
    else:
        dept_count[dept] = 1

print(dept_count) 
