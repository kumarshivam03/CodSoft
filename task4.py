import random
def get_user_choice():
    while True:
        user_input = input("Choose rock, paper, or scissors: ").strip().lower()
        if user_input in ["rock", "paper", "scissors"]:
            return user_input
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "User wins"
    else:
        return "Computer wins"
def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"User chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}")

        if result == "User wins":
            user_score += 1
        elif result == "Computer wins":
            computer_score += 1

        print(f"User Score: {user_score}, Computer Score: {computer_score}")

        play_again = input("Do you want to play another round? (yes/no): ").strip().lower()
        if play_again != "yes":
            break
if __name__ == "__main__":
    main()
