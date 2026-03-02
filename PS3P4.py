make = input("Enter make: ")
model = input("Enter model: ")
msrp = float(input("Enter MSRP: "))
discount_percent = float(input("Enter discount percent (e.g., 0.15): "))
amount_off = msrp * discount_percent
discounted_price = msrp - amount_off
print(f"Make: {make}, Model: {model}, MSRP: ${msrp:.2f}, Discount: {discount_percent}, Off: ${amount_off:.2f}, Price: ${discounted_price:.2f}")
