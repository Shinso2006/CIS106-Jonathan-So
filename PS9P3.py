def comp_out_door_price(msrp, make, model, ev_code):
    if make == "Honda" and model == "Accord":
        percent = 0.10
    elif make == "Toyota" and model == "Rav4":
        percent = 0.15
    elif ev_code.upper() == "Y":
        percent = 0.30
    else:
        percent = 0.05
    
    discounted_price = msrp * (1 - percent)
    return discounted_price * 1.07

total_msrp = 0
total_sales_price = 0

response = input("Do you want to run the auto program? (Yes or No): ")
while response.lower() == "yes":
    make = input("Enter Make: ")
    model = input("Enter Model: ")
    ev_code = input("Is it an EV? (Y or N): ")
    msrp = float(input("Enter MSRP: "))
    
    sales_price = comp_out_door_price(msrp, make, model, ev_code)
    total_msrp += msrp
    total_sales_price += sales_price
    
    print(f"Out the door price: ${sales_price:,.2f}")
    
    response = input("Run again? (Yes or No): ")

print(f"\nSummary:\nTotal MSRPs: ${total_msrp:,.2f}\nTotal Sales Prices: ${total_sales_price:,.2f}")
