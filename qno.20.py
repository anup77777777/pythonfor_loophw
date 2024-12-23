num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 % 2 == 0 and num2 % 2 == 0:
    result = num1 + num2
    operation = "sum"
elif (num1 % 2 == 0 and num2 % 2 != 0) or (num1 % 2 != 0 and num2 % 2 == 0):
    result = abs(num1 - num2)
    operation = "difference"

else:
    result = num1 * num2
    operation = "product"
print(f"The {operation} of the two numbers is: {result}")
