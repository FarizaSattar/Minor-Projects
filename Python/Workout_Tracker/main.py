import requests
from datetime import datetime
import os

# User information for calorie calculation
GENDER = "male"
WEIGHT_KG = 84
HEIGHT_CM = 180
AGE = 32

# Nutritionix API credentials (stored in environment variables for security)
APP_ID = os.environ["ENV_NIX_APP_ID"]
API_KEY = os.environ["ENV_NIX_API_KEY"]

# Nutritionix API endpoint
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Ask user to enter exercises they did
exercise_text = input("Please tell me which exercises you did: ")

# Prepare headers and parameters for Nutritionix API request
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

# Make POST request to Nutritionix to get exercise details
response = requests.post(exercise_endpoint, json=parameters, headers=headers)
exercise_data = response.json()

# Print the full response (optional, for debugging)
print("Exercise details received from Nutritionix:")
print(exercise_data)

# Get current date and time to log in Google Sheet
today_date = datetime.now().strftime("%d/%m/%Y")
current_time = datetime.now().strftime("%H:%M:%S")

# Sheety API endpoint (stored in environment variables)
sheet_endpoint = os.environ["ENV_SHEETY_ENDPOINT"]

# Loop through each exercise returned by Nutritionix and send to Google Sheet via Sheety
for exercise in exercise_data["exercises"]:
    # Prepare data to send to Google Sheet
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": current_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # Send POST request to Sheety to add exercise data to Google Sheet
    # Using basic authentication here; replace with your method if needed
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        auth=(
            os.environ["ENV_SHEETY_USERNAME"],
            os.environ["ENV_SHEETY_PASSWORD"]
        )
    )

    # Print Sheety response to check if data was successfully added
    print("Response from Sheety API:")
    print(sheet_response.text)
