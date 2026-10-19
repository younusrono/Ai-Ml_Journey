class laptop:
    storage_type = "ssd"
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage
        
    @classmethod
    def get_storage_type(cls): 
        print(f"storage type = {cls.storage_type}")
        
    def get_info(self):
        print(f"laptop has {self.ram} ram & {self.storage} {self.storage_type}")

l1 = laptop("16gb", "512gb")
l1.get_storage_type() 
l1.get_info()

# @classmethod হলো এমন একটা method যেটা object-এর বদলে class-এর সাথে কাজ করে।
