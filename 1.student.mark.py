def student_num():
    return int(input("Input number of students in a class:"))

def student_info():
    student_id=input("Input student ID:")
    student_name=input("Input student name:")
    student_dob=input("Input student DoB:")
    return {"id":student_id,"name":student_name,"dob":student_dob}

def course_num():
    return int(input("Input number of courses:"))

def course_info():
    course_id=input("Input the course id:")
    course_name=input("Input the course name:")
    return {"id":course_id,"name":course_name}

def input_marks(courses, students, marks, course_id):
    if course_id not in courses:
        print("Error!!!!")
        return
    
    for student in students:
        mark=float(input("Input marks for {students['name']} in {course[course_id]['name']}"))
        marks.append({"student_id": student['id'], "course_id": course_id, "mark": mark})

def lists_course(courses):
    print("Course lists:")
    for course in course.values():
        print("{course['id']}:{course['name']}")

def lists_students(students):
    print("Student lists:")
    for student in students:
        print("{student['id']}:{student['name']}")

def show_students_marks(marks,courses,students,course_id):
    if course_id not in courses:
        print("Error!!!")
        return
    
    print("Student marks for {course[course_id]['name']}")
    for mark in marks:
        if mark["course_id"]==course_id:
            student_name = next(student["name"] for student in students if student["id"] == mark["student_id"])
            print("{student_name}:{mark['mark']}")

def main():
    students= []
    courses={}
    marks=[]

    num_students = student_num()
    for _ in range(num_students):
        student = student_info()
        students.append(student)

    num_courses = course_num()
    for _ in range(num_courses):
        course = course_info()
        courses[course["id"]] = course

    lists_course(courses)
    lists_students(students)

    course_id = input("Enter the course ID to input marks: ")
    input_marks(courses, students, marks, course_id)

    lists_course(courses)
    lists_students(students)

    show_students_marks(marks, courses, students, course_id)

if __name__ == "__main__":
    main()