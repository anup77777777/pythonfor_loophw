number = int(input("Enter a number: "))
if number % 2 == 0 and number % 7 == 0:
    print("Double Seven")
elif number % 2 == 0:
    print("Even")
elif number % 7 == 0:
    print("Lucky Seven")
else:
    print(number)
