total_gross = 0
count = 0
response = input("Start employee payroll program? (Yes/No): ")

while response == "Yes":
    name = input("Enter employee last name: ")
    hours = float(input("Enter hours worked: "))
    rate = float(input("Enter pay rate: "))
    
    if hours > 40:
        overtime_hours = hours - 40
        gross_pay = (40 * rate) + (overtime_hours * rate * 1.5)
    else:
        gross_pay = hours * rate
        
    print(f"Employee: {name} | Gross Pay: ${gross_pay:.2f}")
    
    total_gross += gross_pay
    count += 1
    response = input("Enter another employee? (Yes/No): ")

if count > 0:
    print(f"\nTotal Gross Pay: ${total_gross:.2f}")
    print(f"Number of Employees: {count}")
    print(f"Average Pay: ${total_gross/count:.2f}")
