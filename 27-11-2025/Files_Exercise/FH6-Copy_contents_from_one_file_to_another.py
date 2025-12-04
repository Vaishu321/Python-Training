with open("source.txt",'w+') as f:
    f.write("Hello World")
    f.seek(0)
    content=f.read()

with open("backup.txt",'w+') as f:
    f.write(content)

