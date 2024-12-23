age = int(input("Enter your age: "))
gender = input("Enter your gender (M/F): ")
show_type = input("Enter the show type (Matinee/Evening): ")
ticket_price = 0
if age < 12:
    ticket_price = 500 if show_type == "Matinee" else 700
elif 12 <= age < 60:
    if gender == 'M':
        ticket_price = 800 if show_type == "Matinee" else 1000
    elif gender == 'F':
        ticket_price = 700 if show_type == "Matinee" else 900
else:  
    ticket_price = 600
print(f"The ticket price is Rs{ticket_price}.")
