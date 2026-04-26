def compute_bowling(g1, g2, g3, handicap):
    avg = (g1 + g2 + g3) / 3
    avg_handicap = avg + handicap
    return avg, avg_handicap

def main():
    lname = input("Enter bowler last name: ")
    g1 = float(input("Game 1 score: "))
    g2 = float(input("Game 2 score: "))
    g3 = float(input("Game 3 score: "))
    handicap = float(input("Enter handicap: "))
    
    avg, h_avg = compute_bowling(g1, g2, g3, handicap)
    
    print(f"\nBowler: {lname}")
    print(f"Average Score: {avg:,.2f}")
    print(f"Handicap Average: {h_avg:,.2f}")

main()
