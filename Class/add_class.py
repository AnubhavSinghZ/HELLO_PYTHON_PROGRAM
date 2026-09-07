#1 first method


class Calculator:
    def __init__(self, num1, num2):
        # Initializing the object's attributes
        self.num1 = num1
        self.num2 = num2

    def add(self):
        # Method performing the addition
        return self.num1 + self.num2

# Instantiating the object
calc = Calculator(10, 5)


print("The sum is:", calc.add())  # Output: The sum is: 15




class Distance:
    def __init__(self, meters):
        self.meters = meters

    # Overloading the '+' operator
    def __add__(self, other):
        # 'self' is the first object, 'other' is the second object
        total_meters = self.meters + other.meters
        # Return a new object containing the combined value
        return Distance(total_meters)

    def __str__(self):
        return f"{self.meters} meters"

# Creating two Distance objects
d1 = Distance(50)
d2 = Distance(30)

# Using the '+' operator directly on objects
result = d1 + d2

print("Combined Distance:", result)  # Output: Combined Distance: 80 meters

