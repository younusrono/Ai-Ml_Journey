# সুবিধা:

# ১. কোড ছোট করে।
# ২. কোড সহজে পড়তে ও বুঝতে সাহায্য করে।
# ৩. সহজে নতুন লিস্ট তৈরি করতে সাহায্য করে।
# ৪. লিস্ট তৈরি করার সময় শর্ত (Condition) ব্যবহার করা যায়।

# List Comprehension ব্যবহার করে সম্পূর্ণ Loop না লিখে,
#  মাত্র এক লাইনের কোডে নতুন List তৈরি করা যায়।

# to print sq value
# code____

# sq=[i*i for i in range(6) if i%2!=0]
# print(sq)


# neg value hole 0 hobe 

# nums=[-2,-3,3,4,-1,7]
# nums=[0 if val<0 else val for val in nums]
# print(nums)

# words=["hello","Rono","Ahmad"]
# words=[val.upper() for val in words]
# print(words)

# Syntax___
# new_list = [expression for item in iterable]

# expression: কী কাজ করতে চাও।
# item: লিস্টের প্রতিটি উপাদান।
# iterable: যে লিস্ট থেকে উপাদান নেবে।

sq=[i*i for i in range(6) if i%2==0]
print(sq)