# We will create a `Student` class that:

# - Stores student name and marks
# - Displays student information (instance method)
# - Shows school name (class method)
# - Counts total students (class variable)

class Student:
    school_name = "ABC School"
    total_students = 0

# Here:

#- `school_name` → shared by all students
# - `total_students` → counts how many students are created

# These are **class variables**.

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        Student.total_students += 1

# Explanation:

# - `name` and `marks` are **instance variables**
# - Every time an object is created,
    #`total_students` increases

    def display_info(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

#This is an **instance method** because:

# - It uses `self`
#- It works on object data

    @classmethod
    def show_school(cls):
        print("School:", cls.school_name)

# This is a **class method** because:

# - It uses `cls`
#- It works on class-level data

s1 = Student("Ram", 85)
s2 = Student("Sita", 92)

# Each object has:
# - Its own name
#- Its own marks

s1.display_info()
print("------")
s2.display_info()

Student.show_school()
print("Total Students:", Student.total_students)

# Learning Outcomes from the Student Management Mini Project:

# - Applied instance methods to manage and display individual student data
# - Used class methods to handle shared information like the school name
# - Tracked shared data using class variables, such as the total number of students
# - Practiced structuring a Python program with classes, objects, and methods for clean, organized code

