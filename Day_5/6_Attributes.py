class student:
    college_name="B.M College"
    # class attribute
    def __init__(self,name,cgpa):
        # instance attribute
        self.name=name
        self.cgpa=cgpa
stu1=student("Rono",3.00)
print(stu1.college_name)
print(student.college_name)


# Class attribute = Same for everyone
# Instance attribute = Different for each object