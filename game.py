import random

def get_player_choice():
    """Get player's choice from input."""
    while True:
        player_choice = input("Enter your choice (Rock/Paper/Scissors) or type 'I quit' to end: ").capitalize()
        if player_choice in ["Rock", "Paper", "Scissors", "I quit"]:
            return player_choice
        else:
            print("Invalid choice. Please choose Rock, Paper, or Scissors.")

def determine_winner(player, computer):
    """Determine the winner of the game."""
    if player == computer:
        return "Game Tied"
    elif (player == "Rock" and computer == "Paper") or \
         (player == "Scissors" and computer == "Rock") or \
         (player == "Paper" and computer == "Scissors"):
        return "You lose"
    else:
        return "You win"

def main():
    actions = ["Rock", "Paper", "Scissors"]

    while True:
        computer_choice = random.choice(actions)
        player_choice = get_player_choice()

        if player_choice == "I quit":
            print("Thank you for playing.")
            break

        print(f"Computer chose: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)

if __name__ == "__main__":
    main()
