username=input("enter username:")
password=input("enter password :")
if(username == "admin" and password=="pass"):
    print("log IN")
else:
    if (username!= "admin"):
        print("wrong username")
    else:
        print("wrong password")
