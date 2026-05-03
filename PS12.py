# PS11_DynamicLists.py

# 1. Prompt for number of items and load integers into a list
num_items = int(input("How many integers would you like to add to the list? "))
list1 = []
for i in range(num_items):
    val = int(input(f"Enter integer {i+1}: "))
    list1.append(val)
print("Initial list:", list1)

# 2. Insert 99 at position 1
list1.insert(1, 99)
print("After inserting 99 at pos 1:", list1)

# 3. Replace 99 with 100
# Find the first occurrence of 99 and change it
if 99 in list1:
    idx = list1.index(99)
    list1[idx] = 100
print("After replacing 99 with 100:", list1)

# 4. Create second list and extend the first
list2 = [500, 600, 700, 800, 900]
print("Second list:", list2)
list1.extend(list2)
print("First list extended:", list1)

# 5. Remove the value 800
if 800 in list1:
    list1.remove(800)
print("After removing 800:", list1)

# 6. Remove the third item (index 2)
if len(list1) >= 3:
    list1.pop(2)
print("After removing third item:", list1)

# 7. Create a list of grades
grades = ["A", "B", "C", "A", "A", "C"]
print("Grades list:", grades)

# 8. Display count of A grades
print("Number of A grades:", grades.count("A"))

# 9. Display index of the first B grade
print("Index of first B grade:", grades.index("B"))

# 10. Look for grade F (without error)
if "F" in grades:
    print("F is in the list")
else:
    print("F is not in the list")

# 11. Clear the second list
list2.clear()
print("Second list cleared:", list2)

# 12. Delete the second list and try to display
# Note: This will cause a NameError as intended by the assignment
del list2
try:
    print(list2)
except NameError:
    print("List2 no longer exists.")

# 13. Create list of players
players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
print("Players:", players)

# 14. Sort and display players
players.sort()
print("Sorted players:", players)

# 15. Make a copy called players2
players2 = players.copy()
print("Players2 (copy):", players2)

# 16. Reverse players2 and display both
players2.reverse()
print("Original players (sorted):", players)
print("Players2 (reversed):", players2)
