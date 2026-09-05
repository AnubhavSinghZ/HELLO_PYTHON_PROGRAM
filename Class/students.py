class Student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
        print("Adding Students and his marks")
s1= Student("Karan", 99)
s2= Student("Arjun", 100)
print(f"{s1.name} and his marks is {s1.marks}")
print(f"{s2.name} and his marks is {s2.marks}")