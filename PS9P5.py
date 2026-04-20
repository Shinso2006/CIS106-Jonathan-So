def comp_assessed_value(county, market_value):
    if county.lower() == "cook":
        percent = 0.90
    elif county.lower() == "dupage":
        percent = 0.80
    elif county.lower() == "mchenry":
        percent = 0.75
    elif county.lower() == "kane":
        percent = 0.60
    else:
        percent = 0.70
    
    return market_value * percent

total_market_value = 0
total_assessed_value = 0

response = input("Do you want to run the assessed value program? (Yes or No): ")
while response.lower() == "yes":
    county = input("Enter County: ")
    market_val = float(input("Enter Market Value: "))
    
    assessed_val = comp_assessed_value(county, market_val)
    
    total_market_value += market_val
    total_assessed_value += assessed_val
    
    print(f"The assessed value for a home in {county} is: ${assessed_val:,.2f}")
    
    response = input("Run again? (Yes or No): ")

print("-" * 30)
print(f"Total of all Market Values:  ${total_market_value:,.2f}")
print(f"Total of all Assessed Values: ${total_assessed_value:,.2f}")
