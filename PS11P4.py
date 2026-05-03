import os

def display_players(names, averages):
    print("\n--- Player Batting Averages ---")
    for i in range(len(names)):
        print(f"Player: {names[i]} | Average: {averages[i]}")

def search_player(names, averages, search_name):
    for i in range(len(names)):
        if names[i].lower() == search_name.lower():
            print(f"Found! {names[i]} has a batting average of {averages[i]}")
            return True
    return False

# Main logic and file loading
if not os.path.exists("players.txt"):
    with open("players.txt", "w") as f:
        f.write("Trout,0.302\nBetts,0.295\nJudge,0.287\nFreeman,0.301\nSoto,0.285\nOhtani,0.274\nAcuna,0.337\nTurner,0.298\nBogaerts,0.307\nDevers,0.283")

player_names = []
batting_avgs = []

with open("players.txt", "r") as file:
    for line in file:
        parts = line.strip().split(",")
        player_names.append(parts[0])
        batting_avgs.append(float(parts[1]))

display_players(player_names, batting_avgs)

while True:
    name_to_find = input("\nEnter player last name to search (or 'done' to stop): ")
    if name_to_find.lower() == 'done':
        break
    search_player(player_names, batting_avgs, name_to_find)
