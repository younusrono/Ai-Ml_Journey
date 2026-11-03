# _____________________Q1____________________

class bankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} TK deposited successfully.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} TK withdrawn successfully.")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print(f"Account Owner: {self.owner_name}")
        print(f"Current Balance: {self.balance} TK")

b1 = bankAccount(10000, "Rahim", 8000)
b1.deposit(2000)
b1.check_balance()


# _____________________Q2____________________

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def count_reviews(self):
        return len(self.reviews)

    def display_all_reviews(self):
        print(f"Reviews for '{self.title}':")
        for review in self.reviews:
            print(f"- {review}")

b = Book("Python Basics", "John Doe")
b.add_review("Great book for beginners!")
b.add_review("Very easy to understand.")

print(f"Total reviews: {b.count_reviews()}")
b.display_all_reviews()

# _____________________Q3____________________

class Student:
    def __init__(self, name, roll_no, marks):
        self.set_name(name)
        self.set_roll_no(roll_no)
        self.set_marks(marks)

    def get_name(self):
        return self._name

    def set_name(self, name):
        if name.strip() != "":
            self._name = name
        else:
            print("Error: Name cannot be empty!")

    def get_roll_no(self):
        return self._roll_no

    def set_roll_no(self, roll_no):
        if 1 <= roll_no <= 100:
            self._roll_no = roll_no
        else:
            print("Error: Roll number must be between 1 and 100!")

    def get_marks(self):
        return self._marks

    def set_marks(self, marks):
        if marks >= 0:
            self._marks = marks
        else:
            print("Error: Marks cannot be negative!")

s1 = Student("Anik", 45, 85)
print(f"Student: {s1.get_name()}, Roll: {s1.get_roll_no()}, Marks: {s1.get_marks()}")

s1.set_marks(-10)
s1.set_roll_no(105)

# _____________________Q4____________________

import math

class Shape:
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

c = Circle(5)
r = Rectangle(4, 5)
t = Triangle(6, 4)

print(f"Circle Area: {c.area():.2f}")
print(f"Rectangle Area: {r.area()}")
print(f"Triangle Area: {t.area()}")


# _____________________Q5____________________


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

my_car = Car("Toyota", "Corolla", 5)
my_bike = Bike("Yamaha", "R15", 155)

print(f"Car: {my_car.brand} {my_car.model}, Seats: {my_car.seats}")
print(f"Bike: {my_bike.brand} {my_bike.model}, Engine CC: {my_bike.engine_cc}")


# _____________________Q6____________________

from abc import ABC, abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self, hours_worked, hourly_rate):
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate

class FullTimeEmployee(Employee):
    def __init__(self, monthly_fixed_salary):
        self.monthly_fixed_salary = monthly_fixed_salary

    def calculate_salary(self):
        return self.monthly_fixed_salary

class ContractEmployee(Employee):
    def __init__(self, contract_amount):
        self.contract_amount = contract_amount

    def calculate_salary(self):
        return self.contract_amount

intern = Intern(80, 200)
full_time = FullTimeEmployee(50000)
contract = ContractEmployee(120000)

print(f"Intern Salary: {intern.calculate_salary()} TK")
print(f"Full-Time Employee Salary: {full_time.calculate_salary()} TK")
print(f"Contract Employee Salary: {contract.calculate_salary()} TK")


# _____________________Q7____________________

class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}, Address: {self.address}")

p1 = Person("Abir")
p2 = Person("Sujon", 25)
p3 = Person("Rifat", 22, "Dhaka")

p1.display()
p2.display()
p3.display()

# _____________________Q8____________________

class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1

p1 = Player("Tamim", 5)
p2 = Player("Shakib", 10)
p3 = Player("Mushfiq", 7)

print(f"Total players created: {Player.player_count}")


# _____________________Q9____________________

class Herbivore:
    def eat_plants(self):
        print("Eating berries and grass.")

class Carnivore:
    def eat_meat(self):
        print("Eating fish and insects.")

class Omnivore:
    def eat_all(self):
        print("Can eat both plants and meat.")

class Bear(Herbivore, Carnivore, Omnivore):
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Bear Name: {self.name}")

b = Bear("Grizzly")
b.display()
b.eat_plants()
b.eat_meat()
b.eat_all()

# _____________________Q10____________________


class User:
    def __init__(self, username):
        self.username = username

class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def display(self):
        return f"{self.sender}: {self.content}"

class ChatRoom:
    def __init__(self, room_name):
        self.room_name = room_name
        self.users = []
        self.messages = []

    def join_user(self, user):
        if user not in self.users:
            self.users.append(user)
            print(f"{user.username} joined the chatroom.")

    def leave_user(self, user):
        if user in self.users:
            self.users.remove(user)
            print(f"{user.username} left the chatroom.")

    def send_message(self, sender, content):
        if sender in self.users:
            msg = Message(sender.username, content)
            self.messages.append(msg)
        else:
            print(f"Error: {sender.username} is not in this chatroom.")

    def view_chat_history(self):
        print(f"\n--- Chat History for {self.room_name} ---")
        for msg in self.messages:
            print(msg.display())

u1 = User("Rohan")
u2 = User("Sara")

room = ChatRoom("Python Developers")

room.join_user(u1)
room.join_user(u2)

room.send_message(u1, "Hello everyone!")
room.send_message(u2, "Hi Rohan! How are you?")

room.view_chat_history()

room.leave_user(u1)
