with open ("PythonFile.txt","w") as f:
    f.write("""Hello World, Python
How is Python
How are you?
Sorry my bad""")

with open ("PythonFile.txt","r") as f:
    f.seek(0)
    content = f.readlines()
    for lines in content:
        if "Python" in lines:
            print(lines)
