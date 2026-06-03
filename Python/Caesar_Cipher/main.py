def caesar_cipher(text, shift, direction):
    result = ""
    
    # If decoding, we will shift letters backwards
    if direction == "decode":
        shift = -shift

    for char in text:
        # Check if the character is a letter
        if char >= 'a' and char <= 'z':
            # Find the position of the letter in the alphabet (0 to 25)
            position = ord(char) - ord('a')
            
            # Shift the position by the shift amount
            new_position = position + shift
            
            # If new_position is less than 0 or greater than 25, wrap around
            if new_position > 25:
                new_position = new_position - 26
            elif new_position < 0:
                new_position = new_position + 26
            
            # Find the new letter and add to result
            new_char = chr(new_position + ord('a'))
            result = result + new_char
        else:
            # If it's not a letter, just add the character as it is
            result = result + char
    
    print("Here is the " + direction + "d message: " + result)

# Welcome message
print("Welcome to the Caesar Cipher program!")

# Start the program loop
while True:
    direction = input("Type 'encode' to encrypt or 'decode' to decrypt:\n").lower()
    
    if direction != "encode" and direction != "decode":
        print("Please type 'encode' or 'decode' only.")
        continue
    
    message = input("Type your message:\n").lower()
    shift = input("Type the shift number:\n")
    
    # Make sure shift is a number
    if not shift.isdigit():
        print("Please enter a valid number for the shift.")
        continue
    
    shift = int(shift) % 26  # Make shift between 0 and 25

    caesar_cipher(message, shift, direction)
    
    again = input("Type 'yes' to go again, or 'no' to quit:\n").lower()
    if again != "yes":
        print("Goodbye! Thank you for using the Caesar Cipher.")
        break
