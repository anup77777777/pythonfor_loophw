price = float(input("Enter the price of the item: "))
if price > 1000:
    discount = 0.10
    final_price = price * (1 - discount)
elif price > 500:
    discount = 0.05
    final_price = price * (1 - discount)
else:
    final_price = price
print(f"The final price after applying the discount is: Rs{final_price:.2f}")
