def display_students(names, scores):
    print("\n--- Student Exam Scores ---")
    for i in range(len(names)):
        print(f"Student: {names[i]} | Score: {scores[i]}")

def display_students_reverse(names, scores):
    print("\n--- Student Exam Scores (Reverse Order) ---")
    for i in range(len(names) - 1, -1, -1):
        print(f"Student: {names[i]} | Score: {scores[i]}")

# Main Logic
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
exam_scores = [85.5, 92.0, 78.0, 88.5, 95.0, 72.0, 81.5, 89.0, 65.0, 99.5]

display_students(last_names, exam_scores)
display_students_reverse(last_names, exam_scores)
