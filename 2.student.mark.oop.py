class Student:
    def __init__(self, student_id, student_name, student_dob):
        self.id = student_id
        self.name = student_name
        self.dob = student_dob

class Course:
    def __init__(self, course_id, course_name):
        self.id = course_id
        self.name = course_name

class MarkSheet:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_student_num(self):
        return int(input("Enter the number of students:"))

    def input_student_info(self):
        student_id = input("Enter the id of the student:")
        student_name = input("Enter the name of the student:")
        student_dob = input("Enter the Dob of the student:")
        return Student(student_id, student_name, student_dob)

    def input_course_num(self):
        return int(input("Enter the number of the courses:"))

    def input_course_info(self):
        course_id = input("Enter the id of the course:")
        course_name = input("Enter the name of the course:")
        return Course(course_id, course_name)

    def input_marks(self, course_id):
        marks = {}
        print("Enter marks for course", course_id)
        for student in self.students:
            mark = int(input(f"Enter the mark for {student.name}:"))
            marks[student.id] = mark
        return marks

    def list_courses(self):
        print("List of courses:")
        for course in self.courses:
            print(f"ID:{course.id}, Name:{course.name}")

    def list_students(self):
        print("List of students:")
        for student in self.students:
            print(f"ID:{student.id}, Name:{student.name}, Dob:{student.dob}")

    def student_marks(self, course_id):
        print(f"Marks for course {course_id}:")
        marks_res = self.marks[course_id]
        for student_id, mark in marks_res.items():
            student_name = next(student.name for student in self.students if student.id == student_id)
            print(f"Student: {student_name}, Mark: {mark}")

    def main(self):
        num_student = self.input_student_num()
        for _ in range(num_student):
            s_info = self.input_student_info()
            self.students.append(s_info)

        num_course = self.input_course_num()
        for _ in range(num_course):
            c_info = self.input_course_info()
            self.courses.append(c_info)

        for course in self.courses:
            course_id = course.id
            self.marks[course_id] = self.input_marks(course_id)

        self.list_courses()
        self.list_students()

        for course_id in self.marks.keys():
            self.student_marks(course_id)

if __name__ == "__main__":
    mark_sheet = MarkSheet()
    mark_sheet.main()
