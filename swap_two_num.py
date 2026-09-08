num1=int(input("Enter the value of number 1="))
num2=int(input("Enter the value of number 2="))

#Method 1 : Using Temporary Variable

temp =num1
num1=num2
num2=temp
print(f"The value of num1 and num2 after swapping is {num1}, {num2} respectively")

#Method 2 : Arithmetic Operators (Addition and Substraction)
number1=int(input("Enter the number1:"))
number2=int(input("enter the number2:"))
number1= number1+number2
number2=number1-number2
number1=number1-number2
print(f"The numbers are {num1} & {num2}")