info = [
    ("Alice", "Math"),
    ("Bob", "Science"),
    ("Alice", "Science"),
    ("Charlie", "Math"),
    ("Bob", "Math"),
    ("Alice", "English"),
    ("Charlie", "English"),
]

# ১. List all unique courses (সেট ব্যবহার করে ইউনিক সাবজেক্ট বের করা)
unique_courses = set(subject for name, subject in info)
print("Unique Courses:", unique_courses)


# ২. List students enrolled in English (যারা English নিয়েছে তাদের লিস্ট)
english_students = [name for name, subject in info if subject == "English"]
print("Students in English:", english_students)


# ৩. Create dictionary (student, set of courses)
student_dict = {}
for name, subject in info:
    if name not in student_dict:
        student_dict[name] = set()
    student_dict[name].add(subject)

print("Student Dictionary:", student_dict)