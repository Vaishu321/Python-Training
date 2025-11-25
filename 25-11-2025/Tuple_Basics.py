
numbers=(10,20,30)
print(numbers.count(10))
names=("Abdullah","Daniel","David")
mixed=(10,"hello",3.5,True)


fruits=("apple","banana","mango")

print(fruits[0])
print(fruits[1])
print(fruits[-1])

nums=(10,20,30,40,50)
print(nums[1:4])
print(nums[:3])
print(nums[::-1]) #reversed tuple

nums=(1,2,3)
#nums[1]=5 ERROR : 'tuple' object does not support item assignment

#Packing and Unpacking Data
data = 10,20,30

a,b,c = data
print(a,b,c)

#nested tuples
employee = ("John",23,("Bangalore","India"))
print(employee[2][0])
