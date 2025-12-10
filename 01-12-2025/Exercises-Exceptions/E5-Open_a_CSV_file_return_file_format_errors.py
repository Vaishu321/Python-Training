try:
    f=open("file.csv","r")
    print(csv.reader(f))
    print("File read successfully")
except FileNotFoundError:
    print("File not found")
except csv.Error:
    print("File Format Error")
