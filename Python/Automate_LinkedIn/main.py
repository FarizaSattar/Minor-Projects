import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

# -------------------- USER CONFIGURATION --------------------

ACCOUNT_EMAIL = "your_email@example.com"       # Replace with your LinkedIn email
ACCOUNT_PASSWORD = "your_password"             # Replace with your LinkedIn password
PHONE = "your_phone_number"                    # Replace with your phone number

# -------------------- SETUP SELENIUM --------------------

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Keeps the browser open after script ends

service = ChromeService(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# -------------------- HELPER FUNCTION --------------------

def abort_application():
    """Cancel the job application if it's too complex."""
    try:
        driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()
        time.sleep(1)
        discard_buttons = driver.find_elements(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
        if discard_buttons:
            discard_buttons[1].click()
            time.sleep(1)
    except NoSuchElementException:
        pass

# -------------------- STARTING SCRIPT --------------------

# Open LinkedIn jobs page (customize the search URL if needed)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords=python&location=London%2C%20United%20Kingdom")
time.sleep(2)

# Reject cookies (if popup appears)
try:
    reject_btn = driver.find_element(By.CSS_SELECTOR, 'button[action-type="DENY"]')
    reject_btn.click()
    time.sleep(1)
except NoSuchElementException:
    pass

# Click "Sign in"
driver.find_element(By.LINK_TEXT, "Sign in").click()
time.sleep(3)

# Fill in login form
driver.find_element(By.ID, "username").send_keys(ACCOUNT_EMAIL)
password_input = driver.find_element(By.ID, "password")
password_input.send_keys(ACCOUNT_PASSWORD)
password_input.send_keys(Keys.ENTER)

# Wait for CAPTCHA to be solved manually
input("After solving CAPTCHA, press Enter to continue...")

# -------------------- JOB APPLICATION PROCESS --------------------

time.sleep(5)
job_listings = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in job_listings:
    print("Opening job listing...")
    listing.click()
    time.sleep(2)

    try:
        # Click "Easy Apply" button
        apply_btn = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_btn.click()
        time.sleep(2)

        # Enter phone number if field is empty
        phone_input = driver.find_element(By.CSS_SELECTOR, "input[id*=phoneNumber]")
        if phone_input.get_attribute("value") == "":
            phone_input.send_keys(PHONE)

        # Check if it's a multi-step application
        submit_btn = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_btn.get_attribute("data-control-name") == "continue_unify":
            abort_application()
            print("Skipped: Complex application.")
            continue

        # Submit the application
        print("Submitting application...")
        submit_btn.click()
        time.sleep(1)

        # Close confirmation popup
        driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss").click()

    except NoSuchElementException:
        abort_application()
        print("Skipped: No easy apply button.")
        continue

# -------------------- END SCRIPT --------------------

print("Job application process complete.")
time.sleep(3)
driver.quit()
