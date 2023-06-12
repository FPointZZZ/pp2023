students = []
courses = []
marks = []

def add_student():
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth: ")
    students.append({'id': id, 'name': name, 'dob': dob})
    print("Student added successfully!")

def add_course():
    id = input("Enter course ID: ")
    name = input("Enter course name: ")
    courses.append({'id': id, 'name': name})
    print("Course added successfully!")

def add_marks():
    student_id = input("Enter the student ID: ")
    course_id = input("Enter the course ID: ")
    student_marks = input("Enter the marks for the student: ")
    marks[(student_id, course_id)] = student_marks
    print("Marks added successfully!")

def list_courses():
    print("Courses:")
    for course in courses:
        print(f"ID: {course['id']}, Name: {course['name']}")

def list_students():
    print("Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}")

def show_marks():
    course_id = input("Enter the course ID: ")
    print(f"Marks for Course '{get_course_name(course_id)}':")
    for student in students:
        student_id = student['id']
        if (student_id, course_id) in marks:
            student_marks = marks[(student_id, course_id)]
            print(f"Student ID: {student_id}, Name: {student['name']}, Marks: {student_marks}")

def get_course_name(course_id):
    for course in courses:
        if course['id'] == course_id:
            return course['name']
    return None

def print_menu():
    print("----- Student Mark Management Menu -----")
    print("1. Add Student")
    print("2. Add Course")
    print("3. Add Marks")
    print("4. List Courses")
    print("5. List Students")
    print("6. Show Student Marks for a Course")
    print("0. Exit")

# Example usage:
while True:
    print_menu()
    option = input("Enter your choice: ")

    if option == "1":
        add_student()
    elif option == "2":
        add_course()
    elif option == "3":
        add_marks()
    elif option == "4":
        list_courses()
    elif option == "5":
        list_students()
    elif option == "6":
        show_marks()
    elif option == "0":
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")
