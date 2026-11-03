# with ব্যবহার করা হয় file-এর কাজ শেষ হলে 
# automatically file close করার জন্য।


with open("Day_6/4_sample.txt","r") as f:
    data=f.read()
    print(len(data))
