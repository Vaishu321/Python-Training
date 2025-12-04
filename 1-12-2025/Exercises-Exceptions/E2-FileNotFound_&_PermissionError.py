try:
    f=open("file.txt","r")
    print(f.read())
except FileNotFoundError:
    print("File Not Found")
except PermissionError:
    print("Permission Denied")
