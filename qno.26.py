age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
membership_type = input("Enter the membership type (Monthly/Yearly): ")
fee = 0
if 18 <= age < 30:
    if gender == 'M':
        fee = 50
    elif gender == 'F':
        fee = 45
elif 30 <= age <= 50:
    fee = 60
elif age > 50:
    fee = 40
if membership_type == 'Yearly':
    fee *= 10
if fee > 0:
    print(f"The membership fee is Rs{fee}.")
else:
    print("Invalid input. Please check the age, gender, and membership type.")
