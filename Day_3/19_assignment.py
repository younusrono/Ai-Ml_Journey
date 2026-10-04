# _____________________Q1____________________

# salary=float(input("enter salary :"))
# if(salary<30000):
#     final=salary*0.05
#     print(final)
# elif(salary<=70000):
#     final_2=salary*0.15
#     print(final_2)
# else:
#     final_3=salary*0.25
#     print(final_3)


# _____________________Q2____________________

# def even(a,b):
#     for i in range(a,b+1):
#         if(i%2==0):
#             print(i)
# even(2,8)

# _____________________Q3____________________

# def digit(n):
#     if n==0:
#         print(0)
#         return
#     while n>0:
#         digit=n%10
#         print(digit)
#         n=n//10
# digit(312)

# _____________________Q4____________________

# def digit(n):
#     if n==0:
#         print(0)
#         return 1
#     count=0
#     while n>0:
#         count=count+1
#         n=n//10
#     return count
# ans=digit(312)
# print(ans)
  

# _____________________Q5____________________

# def digit(n):
#     if n==0:
#         print(0)
#         return 0
#     sum=0
#     while(n>0):
#         digit=n%10
#         sum=sum+digit
#         n=n//10
#     return sum
# result=digit(312)
# print(result)


# _____________________Q6____________________


# for i in range(1,101):
#     if(i%3==0 and i%5==0):
#         print(i)
    

# _____________________Q7____________________

# while True:
#     user = input("enter a number or quit to stop: ")
#     if user == "quit":
#         print("end of the program !")
#         break

#     n = float(input("enter any number :"))
#     if n > 0:
#         print("positive Number")
#     elif n < 0:
#         print("negative number")
#     else:
#         print("zero !")


# _____________________Q8____________________


# sum=lambda a,b:a+b
# print(sum(2,2))

# sub=lambda a,b:a-b
# print(sub(2,2))

# mul=lambda a,b:a*b
# print(mul(2,2))

# div=lambda a,b:a/b
# print(div(2,2))

# _____________________Q9____________________

# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,n):
#         if(n%i==0):
#             return False
#     return True
# print(is_prime(9))
# print(is_prime(7))
 

# _____________________Q10____________________

# Secret_Number =100

# n=int(input("enter any number :"))

# if(n>Secret_Number):
#     print("Too High !")
# elif(n<Secret_Number):
#     print("Too Low !")
# else:
#     print(" Correct Number !!!")

