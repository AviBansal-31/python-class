# __init__.py
# students.py

class Student:
    def __init__(self):
        self.name = ""
        self.section = -1
        self.id = -1
        self.course_grade = ""
        self.major = ""
        self.gender = ""
        self.answers = {}
        self.score = 0

    def grade(self, key):
        self.score = 0
        for k in key:
            if self.answers[k] == key[k]:
                self.score += 1
    def output(self):
        print("name{}\n"
            "section{}\n"
            "id{}\n"
            "course_grade{}\n"
            "major{}\n"
            "gender{}}\n"
            "answers{}\n"
            "score{}\n".format(self.name,self.section,self.id,self.course_grade,self.major,self.gender,self.answers,self.score))
    def read_student_file(file_name):
        students = []
        try:
            with open(file_name,'r') as student_file:
                headers = student_file.readline().split(',')
                # strip replace something
                question_keys = [question.strip() for question in headers[-10:]]
                for line in file:
                    parts = line.strip().split(',')
                    s = Student()
                    s.section = parts[0]
                    s.name = "{} {}".format(parts[2].strip().title(), parts[3].strip().title())
                    s.id = parts[4].strip()
                    s.course_grade = parts[5].strip().upper()
                    s.major = parts[6].strip().upper()
                    s.gender = parts[7].strip().upper()

                    for i, q in enumerate([int(answer.strip()) for answer in parts[-10:]]):
                        s.answers[question_keys[i]] = q
                    students.append(s)
        except Exception as e:
            print("oops")
            print(e)
        return students

# main.py
# in the file of folder
from example_package.students import read_student_file
import example_package.students as students
students = read_student_file("file-student-data.csv")
students[1].output()
print(students)
answer_key = ['Q1':2,
            'Q2':4,
            'Q3':4,
            'Q4':4,
            'Q5':4,
            'Q6':4,
            'Q7':4,
            'Q8':4,
            'Q9':4,
            'Q10':4,]
for i in range(10):
    students[i].grade(answer_key)
    students[i].output()
