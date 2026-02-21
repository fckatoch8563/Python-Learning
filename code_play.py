class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_birth_year(cls, name, birth_year):
        return cls(name, 2026 - birth_year)

    @classmethod
    def from_string(cls, data_string):
        parts = data_string.split(",")
        if len(parts) != 2:
            raise ValueError("Invalid format")
        name = parts[0].strip()
        age = int(parts[1].strip())
        if age < 0:
            raise ValueError("Age must be positive")
        return cls(name, age)

    # Can return subclass or None but not raise exceptions (not recommended)
    # @classmethod
    # def from_id(cls, user_id):
    #     data = database.get(user_id) #
    #     if data is None:
    #         return None  # Can't do this with __init__
    #     return cls(data['name'], data['age'])


# Different ways to create based on what data you have
p1 = Person("Alice", 30)  # Direct
p2 = Person.from_birth_year("Bob", 1995)  # From birth year
p3 = Person.from_string("Charlie, 25")  # From string

print(f"{p1.name}, {p1.age}")
print(f"{p2.name}, {p2.age}")
print(f"{p3.name}, {p3.age}")
