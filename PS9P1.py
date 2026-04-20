def comp_forecast(month, sales):
    if month in ["Jan", "Feb", "Mar"]:
        percent = 0.10
    elif month in ["Apr", "May", "Jun"]:
        percent = 0.15
    elif month in ["Jul", "Aug", "Sep"]:
        percent = 0.20
    else:
        percent = 0.25
    
    return sales * (1 + percent)

response = input("Do you want to run the program? (Yes or No): ")
while response.lower() == "yes":
    name = input("Enter Last Name: ")
    month = input("Enter Month (e.g., Jan): ")
    sales = float(input("Enter Sales: "))
    
    next_month_sales = comp_forecast(month, sales)
    print(f"Next month's forecasted sales for {name}: ${next_month_sales:,.2f}")
    
    response = input("Run again? (Yes or No): ")
