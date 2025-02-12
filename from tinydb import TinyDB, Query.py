from tinydb import TinyDB, Query     #imports database and libraries we are using (double check with Mr Henley this is right)!!!
db = TinyDB('students.json')    #ask Mr Henley to explain
User = Query()      # ask Mr Henley to explain

db.insert({'ID': "001", 'Name':"Roberto", 'Age': 17, 'Grade': "A"})
db.insert({'ID': "002", 'Name':"Carlos", 'Age': 17, 'Grade': "A*"})
db.insert({'ID': "003", 'Name':"Reece", 'Age': 16, 'Grade': "A*"})



def add_student():
    id = str(input("Enter ID: "))
    name = input("Enter name: ")
    age = float(input("Enter age: "))
    grade = str(input("Enter grade: "))
    db.insert({'ID': id, "Name": name, "Age": age, "Grade": grade})    # Insert new student (record) into the database

def search_student():
    student_search = input("Enter name of student: ")
    student = db.search(User.Name == student_search)     #searches database for user which has wanted name and stores User's data under variable 'student'
    print(student)

def search_grade():
    grade_search = input("Grade to search for: ")
    gradestudents = db.search(User.Grade == grade_search)   #searches database for user with same name and stores User data into variable created
    print(gradestudents)

def show_students():  #not sue this does anything
    for name in db:
        print(name)
    
def change_Grade():
    changed = str(input("Enter student's ID of grade to be changed: "))
    new_grade = input("Enter new grade to be changed for: ")

    #Updating the grade in the database
    db.update({'Grade': new_grade}, User.ID == changed)    #changes grade attribute of user with chosen ID
    print("Updated student ID", changed," to new grade: ", new_grade)

def remove():
    removed = input("Enter student ID to be removed from database: ")
    db.remove(User.ID == removed)    #Removes record from database where the User id is wanted
    print("Record of student with ID: ", removed,"has been removed from database")


def bonus_challenge():
    search = str(input("What grade are you counting? "))
    i = 0
    number_of_students = db.search(User.Grade == search)      #variable stores how many students have the wanted grade
    i = len(number_of_students)                               #varibale i will store length (how many records) of previous variable 
    print("Number of students with grade:", search,"are = ", i)

#current area working on to set id as an integer of 4 digits
def get_ID():
    records = db.all
    last_id = max(int(records('ID')) for record in records if 'ID' in record)
    print(f"last id: {last_id}") 
    return last_id

def set_ID():
    def get_ID() + 1:04d




    

run = 'True'
while run == 'True':
    menu = input('''
                  What would you like to do:
                      1. Add Student
                      2. Show all students
                      3. Search students
                      4. Change grade
                      5. Remove record
                      6. Count how many students in grade category
                      7. Exit
                 == ''')
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
    elif menu == '5':
        remove()
    elif menu == '6':
        bonus_challenge()
    elif menu == '7':
        print("Exited")
        run = 'False'
    else:
        print("Not an option")
    
