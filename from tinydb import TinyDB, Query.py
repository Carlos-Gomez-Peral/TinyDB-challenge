from tinydb import TinyDB, Query

db = TinyDB('students.json')
User = Query()

db.insert({'ID': "001", 'Name':"Roberto", 'Age': 17, 'Grade': "A"})
db.insert({'ID': "002", 'Name':"Carlos", 'Age': 17, 'Grade': "A*"})
db.insert({'ID': "003", 'Name':"Reece", 'Age': 16, 'Grade': "A*"})

def add_student():
    id = str(input("Enter ID: "))
    name = input("Enter name: ")
    age = float(input("Enter age: "))
    grade = str(input("Enter grade: "))
    db.insert({'ID': id, "Name": name, "Age": age, "Grade": grade})

def search_student():
    student_search = input("Enter name of student: ")
    student = db.search(User.Name == student_search)
    print(student)

def search_grade():
    grade_search = input("Grade to search for: ")
    gradestudents = db.search(User.Grade == grade_search)
    print(gradestudents)

def show_students():
    for name in db:
        print(name)
    
def change_Grade():
    changed = str(input("Enter student's ID of grade to be changed: "))
    new_grade = input("Enter new grade to be changed for: ")

    #Updating the grade in the database
    db.update({'Grade': new_grade}, User.ID == changed)
    print("Updated student ID", changed," to new grade: ", new_grade)


while True:
    menu = input(""" What would you like to do:
                 1.  Add Student
                 2. Show all students
                 3. Search students
                 4. Change grade
                 == """)
    if menu == '1':
        add_student()
    elif menu == '2':
        show_students()
    elif menu == '3':
        search = input("Are you searching for name or grade?")
        if search == 'name':
            search_student()
        if search == 'grade':
            search_grade()
    elif menu == '4':
        change_Grade()

    else:
        print("Not an option")
    
show_students()
print(db)
