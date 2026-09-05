class Employee:
    company_name="MNC Company"
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary
    def welcome(self):
        print("Hello Sir,", self.name)
    def get_salary(self):
        return self.salary

s1=Employee("XYZ", 100000)
s1.welcome()
print(s1.get_salary())