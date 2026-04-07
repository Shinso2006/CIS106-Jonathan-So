def calc_average(hits, at_bats):
    return hits / at_bats if at_bats > 0 else 0

player_count = 0
while input("Add a player? (Yes/No): ").strip().lower() == "yes":
    name = input("Enter player last name: ")
    hits = int(input("Enter number of hits: "))
    at_bats = int(input("Enter number of at bats: "))
    
    avg = calc_average(hits, at_bats)
    player_count += 1
    
    print(f"Player: {name} | Batting Average: {avg:.3f}")

print(f"Total players entered: {player_count}")
