# Rock Paper Scissors

import random

user_wins = 0
comp_wins = 0

options = ["rock", "paper", "scissors"]

while True:
  user_input = input("Type Rock/Paper/Scissors or 'q' to quit:").lower()
  if user_input == 'q':
    break
  
  if user_input not in ["rock", "paper", "scissors"]:
    continue

  random_no = random.randint(0, 2)
  comp_pick = options[random_no]
  print(f"Computer picked {comp_pick}.")

  if (user_input == 'rock' and comp_pick == 'scissors') or (user_input == 'paper' and comp_pick == 'rock') or (user_input == 'scissors' and comp_pick == 'paper'):
    print("You won!")
    user_wins = user_wins + 1
  elif (user_input == 'rock' and comp_pick == 'paper') or (user_input == 'paper' and comp_pick == 'scissors') or (user_input == 'scissors' and comp_pick == 'rock'):
    print("Comp. wins!")
    comp_wins = comp_wins + 1
  else:
    print("Tie!")

print(f"computer won {comp_wins} games.\nYou won {user_wins} games.")

print("Goodbye")