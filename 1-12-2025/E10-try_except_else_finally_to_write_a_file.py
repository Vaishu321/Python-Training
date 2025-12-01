try:
    f=open("test.txt","w")
    f.write("This is a test file")
    f.close()
except FileNotFoundError:
    print("File does not exist")
else:
    f=open("test.txt","r")
    print(f.read())
    f.close()
finally:
    print("Closing file")
