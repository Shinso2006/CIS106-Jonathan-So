# Input
qty = float(input("Enter quantity: "))

# Processing
if qty >= 1000:
    unit_price = 3.00
else:
    unit_price = 5.00

ext_price = qty * unit_price
tax = ext_price * 0.07
total = ext_price + tax

# Output
print(f"Quantity: {qty}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${ext_price:.2f}")
print(f"Tax: ${tax:.2f}")
print(f"Total: ${total:.2f}")
