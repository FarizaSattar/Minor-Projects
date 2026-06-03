# Print the game introduction
print("Welcome to Treasure Island!")
print("Your mission is to find the treasure.\n")

# First choice
choice1 = input('You are at a crossroad. Where do you want to go? Type "left" or "right": ').lower()

if choice1 == "left":
    # Second choice
    choice2 = input('You come to a lake. There is an island in the middle of the lake. '
                    'Type "wait" to wait for a boat or "swim" to swim across: ').lower()

    if choice2 == "wait":
        # Third choice
        choice3 = input('You arrive at the island safely. There is a house with 3 doors: red, yellow, and blue. '
                        'Which door do you choose? ').lower()

        if choice3 == "red":
            print("Game over! You entered a room full of fire.")
        elif choice3 == "blue":
            print("Game over! You entered a room full of monsters.")
        elif choice3 == "yellow":
            print("Congratulations! You found the treasure and won!")
        else:
            print("Game over! You chose a door that does not exist.")

    elif choice2 == "swim":
        print("Game over! You were attacked by a trout while swimming.")
    else:
        print("Game over! You did not choose a valid option.")

elif choice1 == "right":
    print("Game over! You fell into a hole.")
else:
    print("Game over! You did not choose a valid option.")
