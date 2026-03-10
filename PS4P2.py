# Input
item = input("Enter item (A or B): ")
qty = float(input("Enter quantity: "))

# Processing
if item == "A":
    unit_price = 10.00
else:
    unit_price = 20.00

ext_price = qty * unit_price

# Output
print(f"Item: {item}")
print(f"Unit Price: ${unit_price:.2f}")
print(f"Extended Price: ${ext_price:.2f}")
