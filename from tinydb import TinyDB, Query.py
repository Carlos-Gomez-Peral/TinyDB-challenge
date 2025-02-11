from tinydb import TinyDB, Query
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = float(age)
        self.grade = str(grade)

student1 = Student("Roberto", 17, "A")
student2 = Student("Carlos", 17, "A*")
student3 = Student("Reece", 16, "A*")

print(student2.grade)