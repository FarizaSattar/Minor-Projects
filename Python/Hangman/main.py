import random
from hangman_words import word_list   # Import the list of words
from hangman_art import logo, stages  # Import the ASCII art for logo and hangman stages

def hangman():
    # Print the game logo at the start
    print(logo)
    
    # Randomly choose a word from the word list
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    
    # Create a display with underscores for each letter in the chosen word
    display = ["_"] * word_length
    
    lives = 6  # Number of lives the player has
    end_of_game = False  # Flag to control the game loop
    
    guessed_letters = set()  # Keep track of letters the player has already guessed

    # Game loop: runs until the game ends
    while not end_of_game:
        guess = input("Guess a letter: ").lower()  # Get player's guess and convert to lowercase

        # Check if player has already guessed this letter
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try again.")
            continue  # Skip to the next iteration of the loop

        guessed_letters.add(guess)  # Add the guess to the set of guessed letters

        # Check if the guessed letter is in the chosen word
        if guess in chosen_word:
            # Reveal the letter in the display wherever it appears in the word
            for i in range(word_length):
                if chosen_word[i] == guess:
                    display[i] = guess
        else:
            # Incorrect guess: lose one life
            lives -= 1
            print(f"Wrong guess! You lost a life. Lives remaining: {lives}")
            if lives == 0:
                # Player has no lives left: game over
                end_of_game = True
                print(f"You lose! The word was '{chosen_word}'.")

        # Show the current state of the word with guessed letters and underscores
        print(" ".join(display))
        # Show the hangman ASCII art corresponding to remaining lives
        print(stages[lives])

        # Check if the player has guessed all the letters
        if "_" not in display:
            end_of_game = True
            print("Congratulations! You guessed the word!")

# Run the game if this script is executed directly
if __name__ == "__main__":
    hangman()
