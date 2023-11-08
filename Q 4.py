import random

def play_game():
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose one: (1) Rock, (2) Paper, (3) Scissors")

    choices = ["Rock", "Paper", "Scissors"]

    user_choice = int(input("Enter your choice (1-3): "))


    if user_choice < 1 or user_choice > 3:
        print("Invalid choice. Please try again.")
        return

    user_choice -= 1 

    # Generate computer's choice
    computer_choice = random.randint(0, 2)

    print("You chose:", choices[user_choice])
    print("Computer chose:", choices[computer_choice])

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("Computer wins!")

# Play the game
play_game()