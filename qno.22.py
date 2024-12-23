age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
income = int(input("Enter your income: "))
tax = 0
if 18 <= age < 60:
    if gender == 'M':
        if income > 1000000:
            tax = 0.30
        elif 500000 < income <= 1000000:
            tax = 0.20
        else:
            tax = 0.10
    elif gender == 'F':
        if income > 1000000:
            tax = 0.25
        elif 500000 < income <= 1000000:
            tax = 0.15
        else:
            tax = 0.05
elif age >= 60:
    if income > 1000000:
        tax = 0.20
    else:
        tax = 0.10
tax_amount = income * tax
print(f"The tax amount is Rs{tax_amount:.2f}")
