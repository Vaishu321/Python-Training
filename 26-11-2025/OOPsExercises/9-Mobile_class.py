class Mobile:
    def __init__(self,brand,model,storage):
        self.brand=brand
        self.model=model
        self.storage=storage
    def display(self):
        print("Brand:",self.brand)
        print("Model:",self.model)
        print("Storage:",self.storage,"GB")
        print("Upgraded Storage:",self.upgrade_storage(),"GB")
    def upgrade_storage(self):
        storage_wanted=(input("Is storage wanted:"))
        if storage_wanted=="Yes":
            self.storage=self.storage*2
            return self.storage
        else:
            return self.storage

m1=Mobile("Mi","XI",64)
m1.display()
