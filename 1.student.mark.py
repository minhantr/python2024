def student_num():
    return int(input("Enter the number of students:"))

def student_info():
    student_id=input("Enter the id of the student:")
    student_name=input("Enter the name of the student:")
    student_DoB=input("Enter the Dob of the student:")
    return {'id':student_id,'name':student_name,'Dob':student_DoB}

def course_num():
    return int(input("Enter the number of the courses:"))

def course_info():
    course_id=input("Enter the id of the course:")
    course_name=input("Enter the name of the course:")
    return {'id':course_id,'name':course_name}

def input_marks(course_id,students):
    marks={}
    print("Enter marks for course",course_id)
    for student in students:
        mark=int(input(f"Enter the mark for {student['name']}:"))
        marks[student['id']]=mark
    return marks

def list_courses(courses):
    print("List of courses:")
    for course in courses:
        print(f"ID:{course['id']}, Name:{course['name']}")
    
def list_students(students):
    print("List of students:")
    for student in students:
        print(f"ID:{student['id']}, Name:{student['name']}, Dob:{student['Dob']}")

def student_marks(course_id,marks_res,students):
    print(f"Marks for course {course_id}:")
    for student_id, mark in marks_res.items():
        student_name = next(student['name'] for student in students if student['id'] == student_id)
        print(f"Student: {student_name}, Mark: {mark}")
    
def main():
    students=[]
    courses=[]
    marks={}
    
    num_student=student_num()
    for _ in range(num_student):
        s_info=student_info()
        students.append(s_info)
    
    num_course=course_num()
    for _ in range(num_course):
        c_info=course_info()
        courses.append(c_info)
        
    for course in courses:
        course_id=course['id']
        marks[course_id]=input_marks(course_id,students)

    list_courses(courses)
    list_students(students)
    
    for course_id, mark in marks.items():
        student_marks(course_id,mark,students)

if __name__=="__main__":
    main()    