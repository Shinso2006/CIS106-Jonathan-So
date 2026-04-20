def comp_sq_ft(l, w, h):
    return (2 * l * w) + (2 * l * h) + (2 * w * h)

response = input("Do you want to run the paint calculator? (Yes or No): ")
while response.lower() == "yes":
    l = float(input("Enter Length: "))
    w = float(input("Enter Width: "))
    h = float(input("Enter Height: "))
    
    sq_ft = comp_sq_ft(l, w, h)
    gallons = sq_ft / 50
    print(f"Total Square Footage: {sq_ft}")
    print(f"Gallons of paint needed: {gallons:.2f}")
    
    response = input("Run again? (Yes or No): ")
