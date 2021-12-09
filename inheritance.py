class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        self._fees = None

    # def __str__(self):
    #     return f"{self.name} is {self.age} years old and had a grade of {self.grade}"
    #
    # def __eq__(self, other):
    #     self.name = other.name
    #     self.age = other.age
    #     self.grade = other.grade

    def update_grade(self, maxGrade):
        if self.grade > maxGrade:
            return maxGrade - self.grade
        else:
            return self.grade

    def _update_age(self, YOB):
        if isinstance(self.age, int):
            return "correct"
        self.age = 2021 - YOB
        return self.age

    def set_fees(self, charges):
        if charges >= 3000:
            assert type(charges) == int
            self._fees = charges * 2
            return self._fees
        else:
            return charges * 1.4

    def totals_abstract(self):
        if self.age > 30:
            self.age = 45


s1 = Students("jef", 8, 67)
print(s1.set_fees(66463))
print(s1.update_grade(30))
