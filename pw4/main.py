import input
import output

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

    def main(self):
        num_student = input.input_student_num()
        for _ in range(num_student):
            s_info = input.input_student_info()
            self.students.append(s_info)

        num_course = input.input_course_num()
        for _ in range(num_course):
            c_info = input.input_course_info()
            self.courses.append(c_info)

        for course in self.courses:
            course_id = course[0]
            self.marks[course_id] = input.input_marks(self.students)

        output.list_courses(self.courses)
        output.list_students(self.students)

        for course_id, marks in self.marks.items():
            output.student_marks(course_id, marks, self.students)

        student_gpas = {}
        for student_id in [student[0] for student in self.students]:
            marks = [self.marks[course_id][student_id] for course_id in self.marks.keys()]
            gpa = self.calculate_gpa(marks, [3, 3])  # Assuming each course has a credit of 3, and considering only two courses
            student_gpas[student_id] = gpa

        output.print_gpa(student_gpas)

    def calculate_gpa(self, marks, credits):
        total_credits = sum(credits)
        weighted_sum = sum(mark * credit for mark, credit in zip(marks, credits))
        return weighted_sum / total_credits

if __name__ == "__main__":
    mark_sheet = MarkSheet()
    mark_sheet.main()
