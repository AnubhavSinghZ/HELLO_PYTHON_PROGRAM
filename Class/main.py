# Creating CLass
class Student:
   def __init__(self):  #constructor name initialization
      print("Adding new students name")
      print(self) # this will print the self
   name="Krish Kapoor"
# Creating Object (instance)
s1=Student()
print(s1.name) # this will give output with name variable
print(s1) # Object at this and it is same as self as of now

class MyClass:
    x=7
p1=MyClass()
p2=MyClass()
p3=MyClass

print(p1.x)
print(p2.x)
print(p3.x)


class Person:
  pass

# having an empty class definition like this, would raise an error without the pass statement