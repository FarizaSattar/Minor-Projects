import os
import random

# Clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Deal a random card from the deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

# Calculate the score of the given cards
def calculate_score(cards):
    # Check for Blackjack (a 2-card 21)
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 represents Blackjack

    # If score is over 21 and there is an ace (11), count ace as 1 instead
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# Compare scores and decide the game result
def compare_scores(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Both went over 21. You both lose."

    if user_score == computer_score:
        return "It's a draw."

    if user_score == 0:
        return "You win with a Blackjack!"

    if computer_score == 0:
        return "You lose. Computer has a Blackjack."

    if user_score > 21:
        return "You went over 21. You lose."

    if computer_score > 21:
        return "Computer went over 21. You win!"

    if user_score > computer_score:
        return "You win!"

    return "You lose."

# Main game function
def play_blackjack():
    clear_screen()
    print("Welcome to Blackjack!")

    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, 'n' to pass: ").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    # Computer's turn: draw cards until score is at least 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(user_score, computer_score))

    # Ask if user wants to play again
    play_again = input("\nPlay another game? Type 'y' for yes, 'n' for no: ").lower()
    if play_again == 'y':
        play_blackjack()
    else:
        print("Thanks for playing!")

# Start the game
play_blackjack()
