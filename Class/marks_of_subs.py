class Studnet:
    def __init__(self,name, marks):
        self.name = name
        self.marks=marks
    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("Hi", self.name,"Your average marks is:", sum/3)

s1= Studnet("Karan", [99,99,99])
s1.get_avg()

s1.name="Iron Man"  # from here we can directly change the value of attribute
s1.get_avg()