# _____________________Q1____________________


# string=str(input("enter string :"))
# x=string[::-1]
# if(x==string):
#     print(f"{x} is a palindrome ! of {string}")
# else:
#     print(f"{x} is not a palindrome ! of {string}")

# _____________________Q2____________________

# list=[1,2,3,4,5,6]
# sum=0
# avg=0
# for i in list:
#     sum=sum+i
# avg=sum/6
# print(f"average of {list} is {avg}")
    
# _____________________Q3____________________

# list_1=eval(input("enter list_1 :"))
# list_2=eval(input("enter list_2 :"))
# result=list_1+list_2
# result.sort()
# print(result)

# _____________________Q4____________________

# tup=(1,2,3,4,5,6,7,8,9,10)
# num=()
# for i in tup:
#     if(i%2==0):
#         num=num+(i,)
# print(f"even tuple {num}")
  

# _____________________Q5____________________
# শুরুতে একটি খালি ডিকশনারি তৈরি করলাম
# students_marks = {}

# while True:
#     # মেনু ডিসপ্লে করা
#     print("\n--- Menu ---")
#     print("A - Add a student")
#     print("B - Update marks")
#     print("C - Search for a student")
#     print("D - Display all students and marks")
#     print("E - Exit (প্রোগ্রাম বন্ধ করতে)")
    
#     # ইউজারের কাছ থেকে চয়েস নেওয়া (.upper() দিলে ছোট হাতের অক্ষর লিখলেও বড় হাতের হয়ে যাবে)
#     choice = input("Enter your choice (A/B/C/D/E): ").upper()
    
#     # ১. নতুন স্টুডেন্ট যোগ করা
#     if choice == 'A':
#         name = input("Enter student name: ")
#         marks = int(input("Enter marks: "))
#         students_marks[name] = marks
#         print(f"{name} added successfully!")
        
#     # ২. মার্কস আপডেট করা
#     elif choice == 'B':
#         name = input("Enter student name to update marks: ")
#         if name in students_marks:
#             new_marks = int(input("Enter new marks: "))
#             students_marks[name] = new_marks
#             print(f"Marks updated for {name}!")
#         else:
#             print(f"Student '{name}' not found!")
            
#     # ৩. স্টুডেন্ট খোঁজা (Search)
#     elif choice == 'C':
#         name = input("Enter student name to search: ")
#         if name in students_marks:
#             print(f"{name}'s marks: {students_marks[name]}")
#         else:
#             print(f"Student '{name}' not found!")
            
#     # ৪. সব স্টুডেন্ট এবং তাদের মার্কস একসাথে দেখানো
#     elif choice == 'D':
#         if students_marks:
#             print("\n--- Student Records ---")
#             for name, marks in students_marks.items():
#                 print(f"Name: {name}, Marks: {marks}")
#         else:
#             print("The dictionary is empty!")
            
#     # ৫. লুপ থেকে বের হওয়ার জন্য অতিরিক্ত অপশন
#     elif choice == 'E':
#         print("Exiting the program. Goodbye!")
#         break
        
#     else:
#         print("Invalid choice! Please select A, B, C, D, or E.")



# _____________________Q6____________________


# word=["apple","banana","kiwi","cherry","mango"]
# word_lengths={}
# for i in word:
#     word_lengths[i]=len(i)
# print(word_lengths)

# _____________________Q7____________________


# name=str(input("enter name :"))
# space_count=0
# for i in name:
#     if(i==''):
#         space_count+=1
# print(space_count)

# _____________________Q8____________________

# list_1=[1,2,3,4]
# list_2=[5,6,7,8]
# list_1=set(list_1)
# list_2=set(list_2)  
# x=list_1.intersection(list_2)
# print(x)

# _____________________Q9____________________

# # ইনপুট লিস্ট
# my_list = [1, 2, 3, 2, 4, 5, 4, 4, 6]

# seen = set()
# duplicates = set()

# for item in my_list:
#     if item in seen:
#         duplicates.add(item)
#     else:
#         seen.add(item)

# # ফলাফল প্রিন্ট করা
# print("একের অধিকবার থাকা উপাদানগুলো:", list(duplicates))


# _____________________Q10____________________

# x=input("enter a string :")
# unique_x=set(x)
# print(unique_x)
# len_x=len(unique_x)
# print(len_x)