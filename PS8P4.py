def get_pay_rate(job_code):
    rates = {'L': 25, 'A': 30, 'J': 50}
    return rates.get(job_code.upper(), 0)

total_payroll = 0
while input("Enter employee data? (Yes/No): ").strip().lower() == "yes":
    last_name = input("Enter last name: ")
    job_code = input("Enter job code (L, A, J): ")
    hours = float(input("Enter hours worked: "))
    
    rate = get_pay_rate(job_code)
    if hours > 40:
        gross_pay = (40 * rate) + ((hours - 40) * rate * 1.5)
    else:
        gross_pay = hours * rate
        
    total_payroll += gross_pay
    print(f"Employee: {last_name} | Gross Pay: ${gross_pay:,.2f}")

print(f"Total Payroll: ${total_payroll:,.2f}")
