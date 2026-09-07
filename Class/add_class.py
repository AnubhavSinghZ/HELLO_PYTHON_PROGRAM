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

# Calling the function to get the sum
print("The sum is:", calc.add())  # Output: The sum is: 15
