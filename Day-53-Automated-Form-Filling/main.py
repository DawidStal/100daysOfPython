from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from bs4 import BeautifulSoup
import os
import dotenv
import requests
import re

dotenv.load_dotenv()

form_url = os.getenv("FORM-URL")
site_url = os.getenv("SITE-URL")
response = requests.get(site_url)
listing_data = []
soup = BeautifulSoup(response.text,"html.parser")
listings = soup.find_all("div", class_="StyledPropertyCardDataWrapper")
print(len(listings))
for listing in listings:
    price = listing.find("span", class_="PropertyCardWrapper__StyledPriceLine").getText().strip()
    link_element = listing.find("a", class_="StyledPropertyCardDataArea-anchor")
    link = link_element.get("href")
    address = link_element.getText().strip()
    price = re.split(r"(\+|/)", price)[0].strip()
    print(price)
    print(link)
    print(address)
    listing_data.append({
        "price": price,
        "link": link,
        "address": address
    })

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 3)
driver.get(form_url)
wait.until(ec.presence_of_element_located((By.TAG_NAME, 'form')))
for entry in listing_data:
    address_element = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-params*="Address of the property"]')))
    price_element = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-params*="Price per month"]')))
    link_element = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-params*="Link"]')))
    address_element.find_element(By.TAG_NAME, "input").send_keys(entry["address"])
    price_element.find_element(By.TAG_NAME, "input").send_keys(entry["price"])
    link_element.find_element(By.TAG_NAME, "input").send_keys(entry["link"])
    submit_button = wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div[role='button']")))
    submit_button.click()
    another_response = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "c2gzEf"))).find_element(By.TAG_NAME,"a")
    another_response.click()

driver.quit()
