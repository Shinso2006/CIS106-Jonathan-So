def compute_total(quantity, price):
    total = quantity * price
    if total > 10000:
        total = total * 0.90
    return total

while True:
    do_program = input("Do you want to run the program? (Yes/No): ").strip().lower()
    if do_program != "yes":
        break
        
    qty = float(input("Enter quantity: "))
    unit_price = float(input("Enter price: "))
    
    final_total = compute_total(qty, unit_price)
    
    print(f"Quantity: {qty}")
    print(f"Price: ${unit_price:,.2f}")
    print(f"Extended Price (with discount if applicable): ${final_total:,.2f}\n")
