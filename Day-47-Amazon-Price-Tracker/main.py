import requests
import os
import dotenv
import smtplib
from bs4 import BeautifulSoup

dotenv.load_dotenv()

SMTP_EMAIL_FROM = os.getenv("SMTP_EMAIL_FROM")
SMTP_EMAIL_TO = os.getenv("SMTP_EMAIL_TO")
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}
response = requests.get(
    "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1",
    headers=headers
)
soup = BeautifulSoup(response.text, "html.parser")
price = soup.select_one(".a-price .a-offscreen").get_text(strip=True).split("$")[1]
print(f"Price: {price}")

if (float(price) < 1):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=SMTP_EMAIL_FROM, password=SMTP_PASSWORD)  
        connection.sendmail(
            from_addr=SMTP_EMAIL_FROM,
        to_addrs=SMTP_EMAIL_TO,
        msg=f"Subject:Amazon Price Tracker\n\nThe price of the Instant Pot has dropped to ${price}!"
    )