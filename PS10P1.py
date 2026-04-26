def compute_discount(qty, price, rate):
    discount_amount = price * rate
    discounted_price = price - discount_amount
    return discount_amount, discounted_price

def main():
    qty = float(input("Enter quantity: "))
    price = float(input("Enter price: "))
    rate = float(input("Enter discount rate (e.g., 0.10 for 10%): "))
    
    disc_amt, disc_price = compute_discount(qty, price, rate)
    
    print(f"\nQuantity: {qty}")
    print(f"Original Price: ${price:,.2f}")
    print(f"Discount Amount: ${disc_amt:,.2f}")
    print(f"Discounted Price: ${disc_price:,.2f}")

main()
