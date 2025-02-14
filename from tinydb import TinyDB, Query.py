from tinydb import TinyDB, Query     #imports database and libraries we are using (double check with Mr Henley this is right)!!!
db = TinyDB('students.json')    #ask Mr Henley to explain
User = Query()      # ask Mr Henley to explain

def insert_students():
    db.insert({'ID': "00001", 'Name':"Roberto", 'Age': 17, 'Subject': "Accounting", 'Grade': "A"})
    db.insert({'ID': "00002", 'Name':"Carlos", 'Age': 17, 'Subject': "Maths", 'Grade': "A*"})
    db.insert({'ID': "00003", 'Name':"Reece", 'Age': 16, 'Subject': "Computer Sience", 'Grade': "A*"})


def get_id():
    students = db.all()
    if students:
        max_id = max(int(student['ID']) for student in students)
        new_id = f"{max_id + 1:05d}"
    else:
        new_id = '00001'
    return new_id

def add_student():
    id = get_id()
    name = input("Enter name: ")
    age = float(input("Enter age: "))
    grade = str(input("Enter grade: "))
    subject = input("Enter subject: ")
    db.insert({'ID': id, "Name": name, "Age": age, "Subject": subject, "Grade": grade})    # Insert new student (record) into the database
    

def search_grade():
    grade_search = input("Grade to search for: ")
    gradestudents = db.search(User.Grade == grade_search)   #searches database for user with same name and stores User data into variable created
    print(gradestudents)

def show_students():  
    for User in db.all():
        print(User)
    
def change_details():
    selected = input("Enter ID of user with incorrect details")
    changed = str(input('''Which details will you be changing? 
                    - Grade
                    - Name
                    - Subject
                    - Age'''))
    if changed == 'Grade':
        new_grade = input("Enter new grade to be changed for: ")
        db.update({'Grade': new_grade}, User.ID == selected)    #changes grade attribute of user with chosen ID
        print("Updated student", changed," to correct grade: ", new_grade)
    elif changed == 'Name':
        new_name = input("Enter coorrect name: ")
        db.update({'Name': new_name}, User.ID == selected)
        print("Updated student ", changed," to correct name: ", new_name)
    elif changed == 'Subject':
        new_subject = input("Enter new subject")
        db.update({'Subject': new_subject}, User.ID == selected)
        print("Updated student ", changed," to correct subject: ", new_subject)
    elif changed == 'Age':
        new_age = float(input("Enter correct age"))
        db.update({'Age': new_age}, User.ID == selected)
        print("Updated student", changed," to correct age: ", new_age)
    

    #Updating the grade in the database
    

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


def set_id():
    records = db.all()            #current area working on to set id as an integer of 4 digits
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    

insert = input("Would you like to insert students: ")
if insert == 'yes':
    insert_students()


run = 'True'
while run == 'True':
    menu = input('''
                  What would you like to do:
                      1. Add Student
                      2. Show all students
                      3. Search students
                      4. Change student details
                      5. Remove record
                      6. Count how many students in grade category
                      7. Exit
                 == ''')
    if menu == '1':
        add_student()
    elif menu == '2':
        show_students()
    elif menu == '3':
        search_grade()
    elif menu == '4':
        change_details()
    elif menu == '5':
        remove()
    elif menu == '6':
        bonus_challenge()
    elif menu == '7':
        print("Exited")
        run = 'False'
    else:
        print("Not an option")
    
    

