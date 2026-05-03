import os

def display_players(names, averages):
    print("\n--- Player Database ---")
    for i in range(len(names)):
        print(f"{names[i]}: {averages[i]}")

def search_with_error(names, averages, search_name):
    found = False
    for i in range(len(names)):
        if names[i].lower() == search_name.lower():
            print(f"Result: {names[i]} - Average: {averages[i]}")
            found = True
            break # Stop searching once found
    
    # Problem 5 Requirement:
    if not found:
        print("Name not found")

# Main logic
if not os.path.exists("players.txt"):
    with open("players.txt", "w") as f:
        f.write("Trout,0.302\nBetts,0.295\nJudge,0.287\nFreeman,0.301\nSoto,0.285\nOhtani,0.274\nAcuna,0.337\nTurner,0.298\nBogaerts,0.307\nDevers,0.283")

player_names = []
batting_avgs = []

with open("players.txt", "r") as file:
    for line in file:
        name, avg = line.strip().split(",")
        player_names.append(name)
        batting_avgs.append(float(avg))

display_players(player_names, batting_avgs)

while True:
    user_input = input("\nSearch for a player (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break
    search_with_error(player_names, batting_avgs, user_input)
