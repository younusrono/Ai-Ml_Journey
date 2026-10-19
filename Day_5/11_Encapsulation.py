class bankaccount:
    def __init__(self,name,balance):
        self.name=name
        self.__balance=balance

# self._balance → Protected (convention অনুযায়ী)
# self.__balance → Private (name mangling ব্যবহার করে)
    def get_balance(self):
        return self.__balance
    def set__balance(self,newbalance):
        self.__balance=newbalance

b1=bankaccount("rono",10000)
b1.set__balance(200000)
print(b1.get_balance())

