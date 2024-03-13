import math

def input_student_num():
    return int(input("Enter the number of students:"))

def input_student_info():
    student_id = input("Enter the id of the student:")
    student_name = input("Enter the name of the student:")
    student_dob = input("Enter the Dob of the student:")
    return student_id, student_name, student_dob

def input_course_num():
    return int(input("Enter the number of the courses:"))

def input_course_info():
    course_id = input("Enter the id of the course:")
    course_name = input("Enter the name of the course:")
    return course_id, course_name

def input_marks(students):
    marks = {}
    for student in students:
        mark = float(input(f"Enter the mark for {student[1]}:"))
        mark = math.floor(mark * 10) / 10  # Round down to 1 decimal using floor
        marks[student[0]] = mark
    return marks
