from utils import *

students = []

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        roll_no = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        marks = float(input("Enter Marks: "))

        student = {
            "roll_no": roll_no,
            "name": name,
            "marks": marks
        }

        add_student(students, student)
        print("Student added successfully!")

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        roll_no = int(input("Enter Roll Number to search: "))
        student = search_student(students, roll_no)

        if student:
            print(student)
        else:
            print("Student not found!")

    elif choice == "4":
        roll_no = int(input("Enter Roll Number to update: "))
        new_name = input("Enter New Name: ")
        new_marks = float(input("Enter New Marks: "))

        if update_student(students, roll_no, new_name, new_marks):
            print("Student updated successfully!")
        else:
            print("Student not found!")

    elif choice == "5":
        roll_no = int(input("Enter Roll Number to delete: "))

        if delete_student(students, roll_no):
            print("Student deleted successfully!")
        else:
            print("Student not found!")

    elif choice == "6":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")