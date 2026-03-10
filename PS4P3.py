# Input
num_books = int(input("Enter number of books: "))
cost_per_book = float(input("Enter cost per book: "))

# Processing
order_total = num_books * cost_per_book

if order_total > 50.00:
    shipping = 0.00
else:
    shipping = 25.00

# Output
print(f"Order Total: ${order_total:.2f}")
print(f"Shipping Charge: ${shipping:.2f}")
