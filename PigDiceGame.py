import random

def roll():
    min_val = 1
    max_val = 6
    roll = random.randint(min_val, max_val)
    return roll

print(roll())

while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be b/w (2 - 4)!")
    else:
        print("Invaild input!")

max_score = 50
player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn:")
        print(f"Your total score is {player_scores[player_idx]}\n")
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != 'y':
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1, so your turn is over!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
            
            print("Your current score is:", current_score)
        player_scores[player_idx] += current_score
        print(f"\nYour total score is {player_scores[player_idx]}")

max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"\nPlayer {winning_idx + 1} is the winner!")