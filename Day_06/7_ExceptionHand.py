try:
    x=int(input("enter the x:"))
    ans=10/x
except ZeroDivisionError:
    print(f"Divide by zero is not allow !")
except ValueError:
    print(f"Invalid Input !")
else:
    print(ans)