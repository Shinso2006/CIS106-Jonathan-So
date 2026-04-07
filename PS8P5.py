def calc_tuition(credits, district_code):
    rate = 250 if district_code.upper() == 'I' else 550
    return credits * rate

while input("Calculate tuition for a student? (Yes/No): ").strip().lower() == "yes":
    name = input("Enter student last name: ")
    credits = float(input("Enter credit hours: "))
    code = input("Enter district code (I/O): ")
    
    tuition = calc_tuition(credits, code)
    print(f"Student: {name} | Credits: {credits} | Tuition Owed: ${tuition:,.2f}")
