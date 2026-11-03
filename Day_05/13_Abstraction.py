from abc import ABC , abstractmethod

class animal(ABC):
    @abstractmethod
    def sound(self):
        pass
class lion(animal):
    def sound(self):
        print("roar !")
l1=lion()
l1.sound()

# শুধু কী করতে হবে সেটা নির্ধারণ করা, 
# কিন্তু কীভাবে করতে হবে সেটা child class-এর ওপর ছেড়ে দেওয়া—এটাই Abstraction-এর মূল ধারণা।