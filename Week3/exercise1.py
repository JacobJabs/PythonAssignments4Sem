class Student(): 
    def __init__ (self, name: str, gender: str, data_sheet: DataSheet, image_url: str)
    self.name = name
    self.gender = gender
    self.data_sheet = data_sheet
    self.image_url = image_url

     def get_avg_grade(self):
        grades = self.data_sheet.get_grades_as_list()
        gradesSum = 0
        for x in grades:
            gradesSum += x

        return gradesSum / len(grades)



class DataSheet(): 

    def get_grades_as_list(self):
        grades = []
        for course in getCourses():
            grades.append(course.getGrade())

        return grades



class Course(): 
    def __init__(self, name: str, classroom: str, teacher: str, ects: int, grade: int = None):
        self._name = name
        self._classroom = classroom
        self._teacher = teacher
        self._ects = ects
        self._grade = grade
