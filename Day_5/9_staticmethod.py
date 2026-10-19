class laptop:
    @staticmethod
    def discountprice(price, discount):
        final_price = price - (discount * price / 100)
        print(f"laptop discount_price {final_price}")

laptop.discountprice(40000, 10)


# • Instance Method: প্রথম প্যারামিটার হিসেবে অবশ্যই self দিতে হয়। 
# এটি ক্লাস এবং অবজেক্ট (instance) উভয়ের অ্যাট্রিবিউটই অ্যাক্সেস করতে পারে।


# • Class Method: প্রথম প্যারামিটার হিসেবে অবশ্যই cls দিতে হয়। 
# এটি শুধু ক্লাসের অ্যাট্রিবিউট অ্যাক্সেস করতে পারে। 
# এর উপরে @classmethod ডেকোরেটর ব্যবহার করতে হয়।


# • Static Method: কোনো বাধ্যতামূলক প্রথম প্যারামিটার (self বা cls) লাগে না। 
# এটি ক্লাস বা অবজেক্টের কোনো স্টেট সরাসরি অ্যাক্সেস করতে পারে না (একটি সাধারণ ফাংশনের মতো)। 
# এর উপরে @staticmethod ডেকোরেটর ব্যবহার করতে হয়।