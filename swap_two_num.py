num1=int(input("Enter the value of number 1="))
num2=int(input("Enter the value of number 2="))

#Method 1 : Using Temporary Variable

temp =num1
num1=num2
num2=temp
print(f"The value of num1 and num2 after swapping is {num1}, {num2} respectively")