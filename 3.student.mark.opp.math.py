import math
import numpy as np
import curses

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = {}

class Course:
    def __init__(self, id, name, credits):
        self.id = id
        self.name = name
        self.credits = credits

class ManagementSystem:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def add_student(self):
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        student = Student(id, name, dob)
        self.students.append(student)
        print("Student added successfully!")

    def add_course(self):
        id = input("Enter course ID: ")
        name = input("Enter course name: ")
        credits = int(input("Enter course credits: "))
        course = Course(id, name, credits)
        self.courses.append(course)
        print("Course added successfully!")

    def add_marks(self):
        student_id = input("Enter the student ID: ")
        course_id = input("Enter the course ID: ")
        student_marks = float(input("Enter the marks for the student: "))
        rounded_marks = math.floor(student_marks * 10) / 10
        for student in self.students:
            if student.id == student_id:
                student.marks[course_id] = rounded_marks
                print("Marks added successfully!")
                return
        print("Student not found!")

    def list_courses(self):
        print("Courses:")
        for course in self.courses:
            print(f"ID: {course.id}, Name: {course.name}, Credits: {course.credits}")

    def list_students(self):
        print("Students:")
        for student in self.students:
            print(f"ID: {student.id}, Name: {student.name}, DoB: {student.dob}")

    def show_marks(self):
        course_id = input("Enter the course ID: ")
        print(f"Marks for Course '{self.get_course_name(course_id)}':")
        for student in self.students:
            if course_id in student.marks:
                student_marks = student.marks[course_id]
                print(f"Student ID: {student.id}, Name: {student.name}, Marks: {student_marks}")

    def calculate_gpa(self, student_id):
        student = self.get_student(student_id)
        if student is None:
            print("Student not found!")
            return

        total_credits = 0
        weighted_sum = 0

        for course_id, marks in student.marks.items():
            course = self.get_course(course_id)
            if course is None:
                continue
            credits = course.credits
            total_credits += credits
            weighted_sum += marks * credits

        if total_credits == 0:
            print("No courses found for the student.")
            return

        gpa = weighted_sum / total_credits
        return round(gpa, 2)

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: self.calculate_gpa(student.id), reverse=True)

    def get_student(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def get_course(self, course_id):
        for course in self.courses:
            if course.id == course_id:
                return course
        return None

    def print_menu(self):
        print("----- Student Mark Management Menu -----")
        print("1. Add Student")
        print("2. Add Course")
        print("3. Add Marks")
        print("4. List Courses")
        print("5. List Students")
        print("6. Show Student Marks for a Course")
        print("7. Calculate Average GPA for a Student")
        print("8. Sort Students by GPA")
        print("0. Exit")

    def run(self):
        while True:
            self.print_menu()
            option = input("Enter your choice: ")

            if option == "1":
                self.add_student()
            elif option == "2":
                self.add_course()
            elif option == "3":
                self.add_marks()
            elif option == "4":
                self.list_courses()
            elif option == "5":
                self.list_students()
            elif option == "6":
                self.show_marks()
            elif option == "7":
                student_id = input("Enter the student ID: ")
                gpa = self.calculate_gpa(student_id)
                if gpa is not None:
                    print(f"Average GPA for Student '{student_id}': {gpa}")
            elif option == "8":
                self.sort_students_by_gpa()
                print("Students sorted by GPA:")
                for student in self.students:
                    print(f"ID: {student.id}, Name: {student.name}, GPA: {self.calculate_gpa(student.id)}")
            elif option == "0":
                print("Exiting the program.")
                break
            else:
                print("Invalid option. Please try again.")


# Example usage:
mark_system = ManagementSystem()
mark_system.run()