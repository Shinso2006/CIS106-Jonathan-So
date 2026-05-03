def display_high_low(names, scores):
    high_var = 0
    high_index = 0
    low_var = 999
    low_index = 0

    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
        
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i

    print(f"\nHighest Score: {names[high_index]} with {scores[high_index]}")
    print(f"Lowest Score: {names[low_index]} with {scores[low_index]}")

# Running the function using arrays from above
display_high_low(last_names, exam_scores)
