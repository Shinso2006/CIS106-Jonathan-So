a, b = 1, 1
print("Fibonacci Sequence (First 20):")
for _ in range(20):
    print(a, end=", " if _ < 19 else "\n")
    a, b = b, a + b
