# Input
appliance = input("Enter appliance name: ")
cost = float(input("Enter cost of appliance: "))

# Processing
if cost > 1000:
    warranty = cost * 0.10
else:
    warranty = cost * 0.05

total = cost + warranty

# Output
print(f"Appliance: {appliance}")
print(f"Cost: ${cost:.2f}")
# Fixed a typo here:
print(f"Warranty Cost: ${warranty:.2f}")
print(f"Total: ${total:.2f}")
