# function overriding :::

class employee:
    def get_designation(self):
        print("designation=Employee !")
class teacher(employee):
    def get_designation(self):
        print("designation=Teacher !")

# e1=employee()
# e1.get_designation

t1=teacher()
t1.get_designation()