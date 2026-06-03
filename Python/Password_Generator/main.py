import random

# Lists of characters to use in the password
letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

print("Welcome to the Password Generator!")

# Get the number of letters, symbols, and numbers from the user
num_letters = int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

# Create an empty list to hold the characters of the password
password_chars = []

# Add random letters to the password list
for _ in range(num_letters):
    password_chars.append(random.choice(letters))

# Add random symbols to the password list
for _ in range(num_symbols):
    password_chars.append(random.choice(symbols))

# Add random numbers to the password list
for _ in range(num_numbers):
    password_chars.append(random.choice(numbers))

# Shuffle the list to mix letters, symbols, and numbers
random.shuffle(password_chars)

# Join the list into a single string
password = ''.join(password_chars)

# Show the generated password
print("Your password is:", password)
