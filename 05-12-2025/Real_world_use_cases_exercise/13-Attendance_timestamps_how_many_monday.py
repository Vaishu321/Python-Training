from datetime import datetime, timedelta
timestamps = [
    "2025-12-05 09:15:00",
    "2025-12-06 10:02:30",
    "2025-12-07 08:45:00",
    "2025-12-08 08:45:00",
    "2025-12-09 08:48:00",
    "2025-12-10 08:49:00",
    "2025-12-11 08:45:00",
    "2025-12-12 08:45:00",
    "2025-12-13 08:45:00",
    "2025-12-14 08:45:00",
    "2025-12-15 08:45:00",
    "2025-12-16 08:45:00",
]
count=0
for i in timestamps:
    dt = datetime.fromisoformat(i)
    if dt.strftime("%A")=="Monday":
        count+=1
print("No. of mondays:",count)