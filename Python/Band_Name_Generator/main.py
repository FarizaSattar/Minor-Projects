def generate_band_name():
    print("Welcome to the Band Name Generator!")

    # Ask the user for the city they grew up in
    city = input("What city did you grow up in?\n")

    # Ask the user for the name of their pet
    pet = input("What is the name of your pet?\n")

    # Combine the city and pet name to create a band name
    band_name = city + " " + pet
    print("Your band name could be: " + band_name + "!")

# Call the function only if this file is run directly
if __name__ == "__main__":
    generate_band_name()
