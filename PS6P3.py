count = 0
response = input("Do you want to do this program? (Yes/No): ")

while response == "Yes":
    last_name = input("Enter student last name: ")
    score1 = float(input("Enter exam score 1: "))
    score2 = float(input("Enter exam score 2: "))
    
    average = (score1 + score2) / 2
    print(f"Student: {last_name} | Average: {average:.2f}")
    
    count += 1
    response = input("Do you want to enter another student? (Yes/No): ")

print(f"Total number of students entered: {count}")
