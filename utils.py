def add_student(students, student):
    students.append(student)


def view_students(students):
    if not students:
        print("No students found")
        return

    for student in students:
        print(student)


def search_student(students, roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            return student
    return None


def update_student(students, roll_no, new_name, new_marks):
    for student in students:
        if student["roll_no"] == roll_no:
            student["name"] = new_name
            student["marks"] = new_marks
            return True
    return False


def delete_student(students, roll_no):
    for student in students:
        if student["roll_no"] == roll_no:
            students.remove(student)
            return True
    return False