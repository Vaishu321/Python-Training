import csv
from csv import DictReader

with open("students_courses.csv","r") as f:
    reader = DictReader(f)
    for row in reader:
        name = row["Name"]
        course = row["Courses"]
        Welcome_letter = f"""Hey {name}, We welcome you on this journey of {course} Degree.
        Hoping you will have great experiences in here with us. Good Luck. """
        with open(f"WelcomeLetter_{name}.txt", "w") as c:
            c.write(Welcome_letter)
