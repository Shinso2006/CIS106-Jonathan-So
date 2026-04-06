# Assuming 'students.txt' exists with format: Name \n Code \n Credits
total_tuition = 0
student_count = 0

try:
    with open("students.txt", "r") as f:
        while True:
            name = f.readline().strip()
            if not name: break
            code = f.readline().strip().upper()
            credits = int(f.readline().strip())
            
            rate = 250.00 if code == 'I' else 500.00
            tuition = credits * rate
            
            total_tuition += tuition
            student_count += 1
            
            print(f"Student: {name} | Credits: {credits} | Tuition: ${tuition:,.2f}")
            
    print(f"\nTotal Tuition Owed: ${total_tuition:,.2f} | Total Students: {student_count}")
except FileNotFoundError:
    print("Please create 'students.txt' first.")
