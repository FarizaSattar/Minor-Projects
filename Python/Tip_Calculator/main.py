def calculate_tip():
    print("Welcome to the tip calculator!")

    # Get user inputs
    total_bill = float(input("What is the total bill? $"))
    tip_percent = int(input("What percentage tip would you like to give? "))
    number_of_people = int(input("How many people are splitting the bill? "))

    # Calculate the tip as a decimal
    tip_decimal = tip_percent / 100

    # Calculate the total bill including tip
    total_with_tip = total_bill * (1 + tip_decimal)

    # Divide the total by the number of people
    amount_per_person = total_with_tip / number_of_people

    # Format the result to 2 decimal places
    final_amount = round(amount_per_person, 2)

    # Display the result
    print("Each person should pay: $" + str(final_amount))

# Run the function
if __name__ == "__main__":
    calculate_tip()
