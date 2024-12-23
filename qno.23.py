age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
score = int(input("Enter your academic score (out of 100): "))
scholarship = "No Scholarship"
if 18 <= age <= 25:
    if gender == 'M':
        if score >= 85:
            scholarship = "Full Scholarship"
        elif score >= 70:
            scholarship = "Partial Scholarship"
    elif gender == 'F':
        if score >= 80:
            scholarship = "Full Scholarship"
        elif score >= 65:
            scholarship = "Partial Scholarship"
print(f"You are eligible for: {scholarship}")
