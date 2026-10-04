age=int(input("enter age :"))
if(age < 13):
    print("child")

# elif(age>13 and age<18):
# print("teenager")

elif(age <18):
    print("teenager")
else:
    print("adult")


# practice ______________ 2:

# username=input("enter the username :")
# password=input("enter the password:")
# if(username=="admin" and password=="pass"):
#     print("LOGIN SUCCESSFUL !")
# elif(username != "admin"):
#     print("wrong Username !")
# else:
#     print("wrong Password !")


n=int(input("enter the number :"))
if(n%5==0):
    print("multiple of 5")
else:
    print("not multiple of 5")