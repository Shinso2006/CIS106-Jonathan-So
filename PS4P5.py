# Input
last_name = input("Enter last name: ")
dependents = int(input("Enter number of dependents: "))
gross_income = float(input("Enter gross income: "))

# Processing
agi = gross_income - (dependents * 12000)

if agi > 50000:
    tax_rate = 0.20
else:
    tax_rate = 0.10

income_tax = agi * tax_rate

if income_tax < 0:
    income_tax = 100

# Output
print(f"Last Name: {last_name}")
print(f"Gross Income: ${gross_income:.2f}")
print(f"Number of Dependents: {dependents}")
print(f"Adjusted Gross Income: ${agi:.2f}")
print(f"Income Tax: ${income_tax:.2f}")
