def compute_sales_data(sales):
    if sales > 100000:
        comm_rate = 0.10
    else:
        comm_rate = 0.05
    
    commission = sales * comm_rate
    target = sales * 0.05
    return commission, target

def main():
    lname = input("Enter salesperson last name: ")
    sales = float(input("Enter sales amount: "))
    
    comm, target = compute_sales_data(sales)
    
    print(f"\nSalesperson: {lname}")
    print(f"Commission: ${comm:,.2f}")
    print(f"Next Year's Target: ${target:,.2f}")

main()
