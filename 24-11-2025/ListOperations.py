fruits=["orange","strawberry","banana"]

fruits[1]="grapes"

print(fruits)

fruits.append("mango")
print(fruits)

fruits.insert(1,"kiwi")
print(fruits)

fruits1 = ["apple","banana","orange"]
fruits1.remove("banana")
print(fruits1)
fruits1.pop(1)
print(fruits1)
fruits1.pop()
print(fruits1)
del fruits[0]
print(fruits1)