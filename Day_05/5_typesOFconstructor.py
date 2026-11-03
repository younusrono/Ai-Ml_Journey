class student:
    # instance attribute beacuse different for other each object
    def __init__(self,name,cgpa):
        # parameterized constructor
        self.name=name
        self.cgpa=cgpa

    # instance method beacuse which are different for specific object 
    def get_cgpa(self):
        return self.cgpa
stu1=student("rono",3.00)
stu2=student("ahmad",3.22)

print(stu1.get_cgpa())