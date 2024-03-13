def list_courses(courses):
    print("List of courses:")
    for course in courses:
        print(f"ID:{course[0]}, Name:{course[1]}")

def list_students(students):
    print("List of students:")
    for student in students:
        print(f"ID:{student[0]}, Name:{student[1]}, Dob:{student[2]}")

def student_marks(course_id, marks_res, students):
    print(f"Marks for course {course_id}:")
    for student_id, mark in marks_res.items():
        student_name = next(student[1] for student in students if student[0] == student_id)
        print(f"Student: {student_name}, Mark: {mark}")

def print_gpa(student_gpas):
    print("\nGPA Scores:")
    for student_id, gpa in student_gpas.items():
        print(f"Student ID: {student_id}, GPA: {gpa:.2f}")
