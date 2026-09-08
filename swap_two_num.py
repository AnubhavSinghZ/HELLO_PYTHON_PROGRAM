#Method 1 : Using Temporary Variable
num1=int(input("Enter the value of number 1="))
num2=int(input("Enter the value of number 2="))
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
print(f"The numbers are {number1} & {number2}")

#Method 3 : Bitwise XOR
mark1=int(input("enter the mark 1 for swap:"))
mark2=int(input("enter the mark 2 for swap:"))
mark1=mark1 ^ mark2
mark2=mark1 ^ mark2
mark1=mark1 ^ mark2
print(f"Mark after swapping mark1={mark1},mark2={mark2}")