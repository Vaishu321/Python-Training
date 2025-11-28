#Default or static
class MathOps:
    def add(self,a,b=0,c=0):
        return a+b+c

m=MathOps()
print(m.add(1))
print(m.add(1,2))
print(m.add(2,3,4))
print(m.add(3,4,5))

#Overloading using *args(Dynamic)
class MathOps:
    def add(self,*args):
        return sum(args)
m=MathOps()
print(m.add(1,2))
print(m.add(2,3,4))
print(m.add(3,4,5))
