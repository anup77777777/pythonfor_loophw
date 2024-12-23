preference = input("Do you want vegetarian or non-vegetarian? ")
if preference == "vegetarian":
    dish = input("Do you want 'Salad' or 'Pasta'? ")
elif preference == "non-vegetarian":
    dish = input("Do you want 'Chicken' or 'Fish'? ")
else:
    dish = "Invalid choice"
print(f"You selected: {dish}")
