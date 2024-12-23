price = float(input("Enter the price of the item: "))
if price > 1000:
    discount = 0.20
    new_price = price * (1 - discount)
elif 500 <= price <= 1000:
    discount = 0.10
    new_price = price * (1 - discount)
else:
    discount = 0.00
    new_price = price
print(f"The new price after applying the discount is: Rs{new_price:.2f}")
