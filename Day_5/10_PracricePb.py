class product:
    count=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
        product.count+=1
    def get_info(self):
        print(f"price of {self.name} is {self.price}")
    @classmethod
    def get_count(cls):
        print(f"total product in store={cls.count}")
    @staticmethod
    def get_discount(price,discount):
        final_price=price-(discount * price / 100)
        print(f"the discount price is {final_price}")    
p1=product("phone",10000)
p2=product("laptop",20_000)
p3=product("pen",10)
p1.get_info()
product.get_count()
p1.get_discount(p1.price,12)