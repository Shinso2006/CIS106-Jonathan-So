def calc_mpg(miles, gallons):
    return miles / gallons

trip_count = 0
while input("Enter a trip? (Yes/No): ").strip().lower() == "yes":
    city = input("Enter destination city: ")
    miles = float(input("Enter miles travelled: "))
    gallons = float(input("Enter gallons used: "))
    
    mpg = calc_mpg(miles, gallons)
    trip_count += 1
    
    print(f"Destination: {city} | Miles: {miles} | MPG: {mpg:.2f}")

print(f"Total trips recorded: {trip_count}")
