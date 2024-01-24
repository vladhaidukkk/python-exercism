from dataclasses import dataclass


@dataclass
class Student:
    name: str
    grade: int
    added: bool


class School:
    def __init__(self):
        self.students: list[Student] = []

    def add_student(self, name, grade):
        for s in self.students:
            if name == s.name:
                added = False
                break
        else:
            added = True
        self.students.append(Student(name, grade, added))

    def roster(self):
        sorted_students = sorted(
            (s for s in self.students if s.added), key=lambda s: (s.grade, s.name)
        )
        return [s.name for s in sorted_students]

    def grade(self, grade_number):
        return sorted(
            s.name for s in self.students if grade_number == s.grade and s.added
        )

    def added(self):
        return [s.added for s in self.students]
