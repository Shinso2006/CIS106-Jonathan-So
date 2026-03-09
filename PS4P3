principle = float(input("Enter principle amount: "))
years = int(input("Enter years to maturity: "))

if principle > 100000 and years == 5:
    rate = 0.06
elif principle >= 50000 and years == 10:
    rate = 0.05
elif principle >= 50000 and years == 5:
    rate = 0.04
else:
    rate = 0.02

interest = principle * rate

print(f"Principle:       ${principle:,.2f}")
print(f"Interest Rate:   {rate:.0%}")
print(f"First Year Int:  ${interest:,.2f}")
