# Define global variables
student_fields = ['ID', 'Name', 'DoB']
course_fields = ['ID','Name']
mark_fields = ['Student ID','Course ID', 'Mark']

def display_menu():
    print(" Welcome to Student Management System!\n Please choose an option as below: ")
    print("0. Exit")
    print("1. Add New Student")
    print("2. Add Course")
    print("3. Add Mark")
    print("4. List Student")
    print("5. List Course")

def add_student():
    print("-------------------------")
    print("Add Student Information")
    global student_fields

    student_data = []
    for field in student_fields:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    print("Data saved successfully")
    input("Press any key to continue")
    return


def add_course():
    print("-------------------------")
    print("Add Course Information")
    global course_fields
    
    course_data = []
    for field in course_fields:
        value = input("Enter " + field + ": ")
        course_data.append(value)
        
    print("Data saved successfully")
    input("Press any key to continue")
    return

def add_mark():
    print("-------------------------")
    print("Add Student's Mark")
    global mark_fields
    
    mark_data = []
    for field in mark_fields:
        value = input("Enter " + field + ": ")
        marks[student_id,course_id] = mark
        mark_data.append(value)
    
    print("Data saved successfully")
    print("Press any key to continue")

def list_student():
    global student_fields

    for student in student_fields:
        print(f"Student's ID: {student[0]}")
        print(f"Student's Name: {student[1]}")
        print(f"Student's DoB: {student[2]}")
    input("Press any key to continue")
    
def list_course():
    global course_fields

    for course in course_fields:
        print(f"Course's ID: {course[0]}")
        print(f"Course's Name: {course[1]}")
    input("Press any key to continue")

while(True):
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        add_course()
    elif choice == '3':
        add_mark()
    elif choice == '4':
        list_student()
    elif choice == '5':
        list_course()
    else:
        break

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")