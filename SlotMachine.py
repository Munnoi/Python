MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("What would you like to deposit? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number!")
    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid number of lines.")
        else:
            print("Please enter a number!")
    return lines

def get_bet():
    while True:
        amount = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_LINES:
                break
            else:
                print(f"Amount must be b/w ({MIN_BET}-{MAX_LINES}).")
        else:
            print("Please enter a number!")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    print(balance, lines)

main()