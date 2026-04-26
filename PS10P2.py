def compute_scores(s1, s2, s3):
    total = s1 + s2 + s3
    avg = total / 3
    return total, avg

def main():
    lname = input("Enter student last name: ")
    s1 = float(input("Enter exam score 1: "))
    s2 = float(input("Enter exam score 2: "))
    s3 = float(input("Enter exam score 3: "))
    
    total, avg = compute_scores(s1, s2, s3)
    
    print(f"\nStudent: {lname}")
    print(f"Total Points: {total}")
    print(f"Average Score: {avg:,.2f}")

main()
