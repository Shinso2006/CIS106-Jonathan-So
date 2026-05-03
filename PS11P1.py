def display_names(names):
    print("\n--- Displaying Names ---")
    for name in names:
        print(name)

def display_names_reverse(names):
    print("\n--- Displaying Names in Reverse ---")
    # range(start, stop, step)
    for i in range(len(names) - 1, -1, -1):
        print(names[i])

# Main Logic
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]

display_names(last_names)
display_names_reverse(last_names)
