class Student:
    def __init__(self, first_name, last_name, district_code, credits):
        self.first_name = first_name
        self.last_name = last_name
        self.district_code = district_code.upper()
        self.credits = credits

    def compute_tuition(self):
        if self.district_code == 'I':
            rate = 250.00
        else:
            rate = 500.00
        
        return self.credits * rate

# Testing the class
def main():
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    dist_code = input("Enter district code (I for In-District, O for Out-of-District): ")
    enrolled_credits = int(input("Enter enrolled credits: "))

    # Instantiate the object
    new_student = Student(f_name, l_name, dist_code, enrolled_credits)

    # Compute and display tuition
    tuition = new_student.compute_tuition()
    
    print("\n--- Student Tuition Invoice ---")
    print(f"Student: {new_student.first_name} {new_student.last_name}")
    print(f"District Status: {'In-District' if new_student.district_code == 'I' else 'Out-of-District'}")
    print(f"Total Tuition Owed: ${tuition:,.2f}")

if __name__ == "__main__":
    main()
