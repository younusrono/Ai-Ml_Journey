class Employee:
    start_time = "10am"
    end_time = "6pm"


class Teacher(Employee):
    def __init__(self, subject):
        self.subject=subject


class AdminStaff(Employee):
    def __init__(self, role):
        self.role = role


teacher = Teacher("Math")
print(teacher.end_time)



