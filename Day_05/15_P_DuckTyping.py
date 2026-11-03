
# Duck Typing কী?

# Python-এ object কোন class-এর, 
# সেটা না দেখে object-এর মধ্যে প্রয়োজনীয় method আছে কি না, 
# সেটা দেখে কাজ করানোকে Duck Typing বলে।

# function overrding and duck_Method main difference : 
# i) function ___ Inheritance lage
# ii) duck   ____ Inheritance lage na

class teacher:
    def get_designation(self):
        print("designation=teacher !")
class student:
    def get_designation(self):
        print("designation=student")

t1=teacher()
s1=student()
t1.get_designation()
s1.get_designation()



# self = object, cls = class,
# আর @staticmethod = নিজে থেকে object বা class পায় না।