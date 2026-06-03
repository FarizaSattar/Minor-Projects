import smtplib
import requests
from bs4 import BeautifulSoup

# ----------------------- USER CONFIGURATION -----------------------
PRODUCT_URL = "https://www.amazon.com/dp/PRODUCT_ID"  # Replace with actual product URL
TARGET_PRICE = 200.00  # Set your desired price to receive alert

YOUR_EMAIL = "your_email@example.com"
YOUR_PASSWORD = "your_email_password"
SMTP_SERVER = "smtp.example.com"  # Example: "smtp.gmail.com"
SMTP_PORT = 587  # Common port for TLS

# ------------------------------------------------------------------

# Set headers to mimic a browser request
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9",
}

# Fetch the product page
response = requests.get(PRODUCT_URL, headers=HEADERS)
soup = BeautifulSoup(response.content, "html.parser")

# Extract product title
title_tag = soup.find(id="productTitle")
title = title_tag.get_text().strip() if title_tag else "No title found"

# Extract product price
price_tag = soup.find(class_="a-price-whole")
if price_tag:
    price_text = price_tag.get_text().replace(",", "").strip()
    try:
        current_price = float(price_text)
    except ValueError:
        current_price = None
else:
    current_price = None

# Check and send email if price is below target
if current_price is not None and current_price < TARGET_PRICE:
    message = f"{title} is now ${current_price:.2f}!\n\nCheck the product here: {PRODUCT_URL}"
    
    with smtplib.SMTP(SMTP_SERVER, port=SMTP_PORT) as connection:
        connection.starttls()
        connection.login(YOUR_EMAIL, YOUR_PASSWORD)
        connection.sendmail(
            from_addr=YOUR_EMAIL,
            to_addrs=YOUR_EMAIL,
            msg=f"Subject:Amazon Price Alert!\n\n{message}"
        )
    print("Price alert sent!")
else:
    print(f"Current price (${current_price}) is above your target price.")
