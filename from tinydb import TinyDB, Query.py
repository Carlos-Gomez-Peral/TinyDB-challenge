from tinydb import TinyDB, Query     #Need to Fully understand first 3 lines of code
db = TinyDB('students.json')    #ask Mr Henley to explain
User = Query()      # ask Mr Henley to explain

def insert_students():  #will enter these 3 records of students into database 
    db.insert({'ID': "00001", 'Name':"Roberto", 'Age': 17, 'Subject': "Accounting", 'Grade': "A"})
    db.insert({'ID': "00002", 'Name':"Carlos", 'Age': 17, 'Subject': "Maths", 'Grade': "A*"})
    db.insert({'ID': "00003", 'Name':"Reece", 'Age': 16, 'Subject': "Computer Sience", 'Grade': "A*"})


def get_id():       #* will set a new id for next function *
    students = db.all()                #stores all records inside databse
    if students:
        max_id = max(int(student['ID']) for student in students)   #converts ID to integer, fetches biggest ID yet.
        new_id = f"{max_id + 1:05d}"    #the use of ' f"{}" ' allows us to make 5 digit value (:05d)
    else:
        new_id = '00001'            #otherwise if no id yet, then set starting ID
    return new_id

def add_student():    #will store a new record of a student based on details entered
    id = get_id()                     #* previous function *
    name = input("Enter name: ")
    age = float(input("Enter age: "))   #made it float just in case
    grade = str(input("Enter grade: "))
    subject = input("Enter subject: ")
    db.insert({'ID': id, "Name": name, "Age": age, "Subject": subject, "Grade": grade})    # Insert new student (record) into the database
    print('''
          ''')
    print(f"{name} has been given ID: {id}")        #to let user know of which ID to search for just in case

def search_grade():     #will allow to search for grade of an ID
    id_search = str(input("ID to search for: "))     
    id_students = db.search(User.ID == id_search)   #seraches database for ID desired
    if id_students:
        student = id_students[0]            #stores first student record from matches found (in case of duplicacy)
        print(student)
        print(f"Student {student['Name']} has grade {student['Grade']}")
    else:
        print("No matches found")

def show_students():    #will print out all students details
    records = db.all()   #stores all current database
    if records:
        for record in records:      #will print any record held inside database
            print(record)
    else:
        print("No records found")
    


def change_details():   #will allow to change any details of an ID(student)
    selected = input("Enter ID of user with incorrect details: ")
    database = db.search(User['ID'] == selected)    #searches for any students with entered ID
    if database:    #used if statement just in case there isn't a match found in database 
        changed = str(input('''Which details will you be changing? 
                    - Grade
                    - Name
                    - Subject
                    - Age
                === '''))
        if changed == 'Grade':
            new_grade = input("Enter new grade to be changed for: ")
            db.update({'Grade': new_grade}, User.ID == selected)    #changes grade attribute of user with chosen ID
            print("Updated student", changed," to correct grade: ", new_grade)
        elif changed == 'Name':
            new_name = input("Enter correct name: ")
            db.update({'Name': new_name}, User.ID == selected)  #updates attribute 'Name' of entered ID
            print("Updated student ", changed," to correct name: ", new_name)
        elif changed == 'Subject':
            new_subject = input("Enter new subject: ")
            db.update({'Subject': new_subject}, User.ID == selected)    ##updates attribute 'Subject' of entered ID
            print("Updated student ", changed," to correct subject: ", new_subject)
        elif changed == 'Age':
            new_age = float(input("Enter correct age: "))
            db.update({'Age': new_age}, User.ID == selected)    #updates attribute 'Age' of entered ID
            print("Updated student", changed," to correct age: ", new_age)
    else:
        print(f"No ID matches found for {selected}")
    

    #Updating the grade in the database
    

def remove():   #will remove wanted record from databse 
    removed = input("Enter student ID to be removed from database: ")
    matches = db.search(User.ID == removed)
    if matches:
        db.remove(User.ID == removed)    #Removes record from database with matching ID entered
        print("Record of student with ID: ", removed,"has been removed from database")
    else:
        print("No matches found")


def bonus_challenge():  #will count how many students are in each grade category
    search = str(input("What grade are you counting? "))
    i = 0
    number_of_students = db.search(User.Grade == search)      #variable stores students matching the wanted grade
    i = len(number_of_students)                               #varibale i will store length (how many records) of previous variable 
    print("Number of students with grade:", search,"are = ", i)

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
# Made insert_students() an if statement to prevent unwanted duplication of the 3 student records
insert = input("Would you like to insert students: ") 
if insert == 'yes':
    insert_students()   #calls back to first function


run = 'True'
while run == 'True':    #Loop will keep running until user chooses to 'Exit'
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
    
    

