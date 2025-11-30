# Write a program that reads a list of student names from students.txt and generates a certificate
# file for each student automatically.
with open ("students.txt","r") as f:
    user = f.read()
    names= user.split()
    for name in names:
        Certificate = f"""This is to certify that {name} has passed his/her 10th grade
    successfully. This certification is to honor the same. """
        with open(f"{name}.txt","w") as f:
            f.write(Certificate)

