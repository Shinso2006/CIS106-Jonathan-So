total = 0.0
tax = 0.0

def compute_totals(qty, unit_price):
    global total
    global tax
    total = qty * unit_price
    tax = total * 0.07

def main():
    qty = float(input("Enter quantity: "))
    u_price = float(input("Enter unit price: "))
    
    compute_totals(qty, u_price)
    
    print(f"\nTotal: ${total:,.2f}")
    print(f"Tax (7%): ${tax:,.2f}")

main()
