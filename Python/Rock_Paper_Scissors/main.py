import random

# ASCII art for rock, paper, scissors
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# List of options for easy access
game_images = [rock, paper, scissors]

def get_user_choice():
    while True:
        choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors:\n")
        if choice.isdigit():
            choice = int(choice)
            if 0 <= choice <= 2:
                return choice
        print("Invalid input. Please enter 0, 1, or 2.")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a draw!"
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_choice = get_user_choice()
    print("You chose:")
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    result = determine_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    play_game()
