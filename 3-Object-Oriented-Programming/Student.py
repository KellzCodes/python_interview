class Student:
    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        Student.all_students.append(self)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, value):
        if not 0 <= value <= 100:
            raise ValueError("New grade not in the accepted range of [0-100]")

        self._grade = value

    @staticmethod
    def calculate_average_grade(students):
        if len(students) == 0:
            return -1

        sum = 0

        for student in students:
            sum += student.grade

        return sum / len(students)

    @classmethod
    def get_average_grade(cls):
        return cls.calculate_average_grade(cls.all_students)

    @classmethod
    def get_best_student(cls):
        if len(cls.all_students) < 1:
            return None

        best_student = None

        for student in cls.all_students:
            if best_student == None or best_student.grade < student.grade:
                best_student = student

        return best_student
