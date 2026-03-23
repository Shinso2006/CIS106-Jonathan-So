total_discounts = 0
response = input("Process an order? (Yes/No): ")

while response == "Yes":
    qty = int(input("Enter quantity: "))
    price = float(input("Enter price: "))
    
    ext_price = qty * price
    
    if ext_price > 10000.00:
        disc_percent = 0.25
    else:
        disc_percent = 0.10
        
    disc_amount = ext_price * disc_percent
    order_total = ext_price - disc_amount
    
    print(f"Extended Price: ${ext_price:.2f}")
    print(f"Discount Amount: ${disc_amount:.2f}")
    print(f"Order Total: ${order_total:.2f}")
    
    total_discounts += disc_amount
    response = input("Process another order? (Yes/No): ")

print(f"\nSum of all discounts: ${total_discounts:.2f}")
