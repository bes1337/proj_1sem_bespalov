#Создайте класс «Студент», который имеет атрибуты имя, фамилия и оценки.
#Добавьте методы для вычисления среднего балла и определения, является ли студент
#отличником.

class Student:
    def __init__(self, name, surname, grades):
        self.name = name
        self.surname = surname
        self.grades = grades

    def average_grade(self):
        avg = sum(self.grades) / len(self.grades)
        return round(avg, 2)

    def is_excellent(self):
        return self.average_grade() >= 4.5


student_1 = Student('Ivan', 'Smirnov', [4, 5, 4])
student_2 = Student('Katya', 'Ivanova', [5, 5, 4])

print(f"Средний балл студента {student_1.name} {student_1.surname}: {student_1.average_grade()}")
print(f"Студент {student_1.name} {student_1.surname} является отличником: {student_1.is_excellent()}")

print()

print(f"Средний балл студента {student_2.name} {student_2.surname}: {student_2.average_grade()}")
print(f"Студент {student_2.name} {student_2.surname} является отличником: {student_2.is_excellent()}")


