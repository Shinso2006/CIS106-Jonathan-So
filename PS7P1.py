while True:
    try:
        principal = float(input("Enter principal amount (or 0 to stop): "))
        if principal == 0: break
        rate = float(input("Enter interest rate (e.g., 0.10): "))
        
        total_interest = 0
        balance = principal
        
        print(f"\n{'Year':<5} {'Beginning Balance':<20} {'Ending Balance':<20}")
        
        for year in range(1, 6):
            beg_balance = balance
            annual_interest = beg_balance * rate
            balance += annual_interest
            total_interest += annual_interest
            print(f"{year:<5} ${beg_balance:,.2f}          ${balance:,.2f}")
            
        print(f"Total interest earned: ${total_interest:,.2f}\n")
    except ValueError:
        print("Please enter numeric values.")
