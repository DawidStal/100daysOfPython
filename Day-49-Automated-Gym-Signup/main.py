from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import os
import time
import dotenv

dotenv.load_dotenv()

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 2)

driver.get("https://appbrewery.github.io/gym/")
driver.find_element(By.ID, "login-button").click()
time.sleep(0.5)

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

def login():
    login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

    email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(email)

    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys(password)

    submit_btn = driver.find_element(By.ID, "submit-button")
    submit_btn.click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))
    print("Found schedule page")

def retry (func, retries=7):
    for i in range(retries):
            try:
                print(f"Trying {func.__name__}. Attempt: {i + 1}")
                return func()
            except TimeoutException:
                if i == retries - 1:
                    print(i, "Retries exhausted")
                    print(retries-1)
                    raise
                time.sleep(1)

retry(login)

print("Logged in")
classes_booked=0
waitlists_joined=0
already_booked_or_waitlisted=0
classes_processed=0

days_to_book = ["Tue", "Thu"]


days = driver.find_elements(By.CSS_SELECTOR, 'div[id^="day-group-"]')
for day in days:
    title = day.find_element(By.CSS_SELECTOR, 'h2[id^="day-title-"]').text
    if any(day_group in title for day_group in days_to_book):
        classes = day.find_elements(By.CSS_SELECTOR, 'div[id^="class-card-"]')
        for class_ in classes:
            classname = class_.find_element(By.CSS_SELECTOR, 'h3[id^="class-name-"]').text
            classtime = class_.find_element(By.CSS_SELECTOR, 'p[id^="class-time-"]').text.replace("Time: ", "")
            if classtime == "6:00 PM":
                print(f"Found {classname} on {title} at {classtime}, attempting to book...")
                button = class_.find_element(By.CSS_SELECTOR, 'button[id^="book-button-"]')
                if button.text == "Booked":
                    already_booked_or_waitlisted += 1
                    print(f"Already booked {classname} on {title} at {classtime}.")
                elif button.text == "Waitlisted":
                    already_booked_or_waitlisted += 1
                    print(f"Already on Waitlist for {classname} on {title} at {classtime}.")
                elif button.text == "Join Waitlist":
                    button.click()
                    classes_processed += 1
                    waitlists_joined += 1
                    print(f"Joined Waitlist for {classname} on {title} at {classtime}.")
                else:
                    button.click()
                    classes_processed += 1
                    classes_booked += 1
                    print(f"Booked {classname} on {title} at {classtime}.")


driver.find_element(By.ID, "my-bookings-link").click()
time.sleep(0.5)
cards = driver.find_elements(By.CSS_SELECTOR, 'div[id*="-card-"]')
verified_count = 0
for card in cards:
    content = card.find_element(By.CSS_SELECTOR, 'div[class^="MyBookings_bookingDetails"]')
    classname = content.find_element(By.CSS_SELECTOR, 'h3[id*="-class-name-"]').text
    details = content.find_elements(By.CSS_SELECTOR, 'p')
    for detail in details:
        if any(day in detail.text for day in days_to_book) and "6:00 PM" in detail.text:
            verified_count += 1
            print(f"Confirmed {classname} at {details[0].text}.")

print(f"--- BOOKING SUMMARY ---\nClasses booked: {classes_booked}\nWaitlists joined: {waitlists_joined}\nAlready booked/waitlisted: {already_booked_or_waitlisted}\nTotal Tuesday 6pm classes processed: {classes_processed}")

if(already_booked_or_waitlisted == verified_count):
    print("All bookings and waitlists verified successfully.")
else:
    print("Some bookings or waitlists could not be verified.")
driver.quit()