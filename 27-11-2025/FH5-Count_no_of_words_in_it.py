with open("notes.txt","r") as f:
    lines=f.read()
    list1= lines.split()
    print("Number of words in file:",len(list1))
