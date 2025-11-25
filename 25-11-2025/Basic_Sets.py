nums={10,20,30,40}

#sets dont allow duplicates
data ={1,2,2,3,3,3}
print(data)

#how to create a set
s2= {10,20,30}
empty = set()
print(empty)

#add operations
s={1,2,3}
s.add(4)
print(s) #correct way to create an empty set
s.update([5,6])
print(s)

#Remove operation
s.remove(1) #raises error if not found
print(s)  #does nothing if not found
s.discard(3)