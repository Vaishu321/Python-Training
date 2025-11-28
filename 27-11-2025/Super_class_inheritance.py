class Person:
    def __init__(self,name):
       self.name=name

class Employee(Person):
    def __init__(self,name,emp_id):
        super().__init__(name) #Parent Constructor
        self.emp_id=emp_id

e=Employee("Eby",101)
print(e.name)
print(e.emp_id)
