# Assuming 'employees.txt' exists with format: Name \n Salary
total_bonuses = 0
try:
    with open("employees.txt", "r") as f:
        while True:
            name = f.readline().strip()
            if not name: break
            salary = float(f.readline().strip())
            
            if salary >= 100000:
                rate = 0.20
            elif salary >= 50000:
                rate = 0.15
            else:
                rate = 0.10
                
            bonus = salary * rate
            total_bonuses += bonus
            print(f"Name: {name} | Salary: ${salary:,.2f} | Bonus: ${bonus:,.2f}")
            
    print(f"\nTotal sum of all bonuses: ${total_bonuses:,.2f}")
except FileNotFoundError:
    print("Please create 'employees.txt' first.")
