import turtle
import pandas

# Set up the screen
screen = turtle.Screen()
screen.title("Canadian Provinces Guessing Game")

# Load the map image of Canada
image = "canadian_provinces_blank.png"  # Ensure this file is in your project folder
screen.addshape(image)
turtle.shape(image)

# Load province data
data = pandas.read_csv("canadian_provinces.csv")
all_provinces = data.province.to_list()

guessed_provinces = []

while len(guessed_provinces) < len(all_provinces):
    answer_province = screen.textinput(title=f"{len(guessed_provinces)}/{len(all_provinces)} Provinces Correct",
                                       prompt="Name a Canadian province or territory:").title()

    if answer_province == "Exit":
        missing_provinces = [prov for prov in all_provinces if prov not in guessed_provinces]
        new_data = pandas.DataFrame(missing_provinces)
        new_data.to_csv("provinces_to_learn.csv")
        break

    if answer_province in all_provinces and answer_province not in guessed_provinces:
        guessed_provinces.append(answer_province)

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        province_data = data[data.province == answer_province]
        t.goto(int(province_data.x), int(province_data.y))
        t.write(answer_province)

# Close the turtle window when done
screen.mainloop()
