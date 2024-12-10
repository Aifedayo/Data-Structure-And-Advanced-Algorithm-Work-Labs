class Employee:
    def __init__(self, name, age, position, salary):
        if age <= 0 or salary <= 0:
            raise ValueError('Age or salary cannot be lesser or equal zero')
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary

    def promote(self):
        self.salary = self.salary * 1.10
        return self.salary
    

emp = Employee('Akeem', 32, 'Team Lead', 6.33)
print(emp.promote())
    