# define a student class
# demands:
# 1 properties includes name,student_id and score of chinese/Eng/Math
# 2 a func can set score of some student's subject
# 3 a func can print all the score of this student

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.grades = {"chi": 0, "math": 0, "eng": 0}

    def setGrades(self, course, grade):
        if course in self.grades.keys():
            self.grades[course] = grade

    def showScores(self):
        print(f"student :{self.name} , id :{self.id} \ngrades:{self.grades} ")


lily = Student("lily", 123)
lily.setGrades("chi", 100)
lily.setGrades("eng", 87)
lily.setGrades("math", 66)

lily.showScores()
