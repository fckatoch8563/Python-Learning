# STATIC METHOD EXAMPLE
# *********************


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):
        return f"{self.name}, {self.position}"

    @staticmethod
    def is_vilid_position(position):
        valid_positions = ["Manager", "Developer", "Designer", "Intern"]
        return position in valid_positions


print(Employee.is_vilid_position("Developer"))  # True
print(Employee.is_vilid_position("CEO"))  # False
############################################################################################
# CLASS METHOD EXAMPLE
# class methods = Allows operations on the class itself, rather than instances
#                 Take (cls) as the first parameter which represents the class itself.


class Student:
    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa

    # Instance Method
    def get_info(self):
        return f"{self.name} {self.gpa}"

    # Class Method
    @classmethod
    def get_count(cls):
        return f"Total count: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average gpa {cls.total_gpa / cls.count:.2f}"


student1 = Student("Sarah", 3.2)
student2 = Student("Bob", 2.0)
student3 = Student("Sandy", 4.0)


print(student1.get_info())
print(student2.get_info())
print(student3.get_info())

print(Student.get_count())
print(Student.get_average_gpa())


##########################################################################
class Student:
    def __init__(self, name, gpa):
        self._name = name  # Single underscore for internal storage
        self._gpa = gpa

    # Getter
    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    # Getter with validation
    @property
    def gpa(self):
        return self._gpa

    @gpa.setter
    def gpa(self, value):
        if not 0.0 <= value <= 4.0:
            raise ValueError("GPA must be between 0.0 and 4.0")
        self._gpa = value


# Usage
student = Student("Sarah", 3.2)
print(student.name)  # Accesses via @property
print(student.gpa)  # Accesses via @property

student.gpa = 3.8  # Uses setter with validation
# student.gpa = 5.0  # Would raise ValueError
