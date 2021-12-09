"""keeps record of names of all workers,
calculates the commision each should get then the total earning for each worker"""
class Workers:
    names = []

    def __init__(self, name, age, salary, role):
        self.name = name
        self.age = age
        """encapsulation"""
        self.__salary = salary  # cannot be accessed directly outside the class methods...try in line 27...encapsulation
        self.role = role
        Workers.names.append(self.get_totals())  # appends result of get_totals
        """abstraction"""

    def __commission(self):  # a level of abstraction this method cannot be accessed outside this class.Can  attempt
        if self.role == 'manager':
            return self.__salary * 0.5
        elif self.role == 'CEO':
            return self.__salary * 0.4
        else:
            return self.__salary * 0.2

    def get_totals(self):  # using the level of abstraction above to determine total earns
        return self.name, self.__commission() + self.__salary


w1 = [Workers("jeff", 15, 300000, "manager"),  # user can input salary btw
      Workers("angayo", 21, 3000, "CEO"),
      Workers("Mwai", 24, 29200, "Chief"),
      Workers("tecno", 23, 8000, " supervisor")]

# print(w1[0].name, w1[0].age, w1[0].role, w1[0].__salary)  # cannot print salary in the w1 list
# print(w1[1].get_totals())

"""inheritance"""


class Manager(Workers):
    def __init__(self, name, age, salary, role, senior_role):
        super().__init__(name, age, salary, role)
        self.senior_role = senior_role

    def get_name_senior_role(self):
        return f"{self.name} is the {self.senior_role} of this company"


m1 = Manager("jeff", 18, 80000, "CEO", "Editor")
print(m1.get_name_senior_role())
print(m1.get_totals())
print(m1.senior_role, m1.role)
print(Workers.names)

