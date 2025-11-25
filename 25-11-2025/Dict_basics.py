student = {
    "name":"john",
    "age":18,
    "city":"Hyderabad"
}
print(student["name"])
print(student["age"])

print(student.get("name"))

#To update Dict.

student["email"] = "test@example.com"
student["city"] = "Dubai"
print(student)

student.pop("age") #remove by key
del student["city"] #delete the key
student.clear() #empty dictionary
print(student)

#To print all the keys
for k in student.keys():
    print (k)
#To print values
for v in student.values():
    print (v)
#To print both keys and values
for k,v in student.items():
    print (k,v)