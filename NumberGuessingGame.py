import random

while True:
    top_of_range = input("Enter the upper range: ")
    if top_of_range.isdigit():
        top_of_range = int(top_of_range) 
        if top_of_range <= 0:
            print("Please type a number greater than 0.")
        else:
            break
    else:
        print("Please type a number.")
random_number = random.randrange(0, top_of_range)
# print(random_number)
guesses = 0 # Keeps track of how many times the user guesses the number
while True:
    user_guess = input("Enter the guess: ")
    guesses += 1
    if user_guess.isdigit():
        user_guess = int(user_guess)
        if user_guess == random_number:
            break
        elif user_guess < random_number:
            print("You were below the number!")
        elif user_guess > random_number:
            print("You were above the number!")
    else:
        print("Please type a number.")

print(f"\nYou finished the game in {guesses} tries!") # Ending statement