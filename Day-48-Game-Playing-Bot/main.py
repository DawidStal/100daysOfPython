import time
from selenium import webdriver
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
t_end=time.time() + 5
t_final=time.time() + 300
driver.get("https://ozh.github.io/cookieclicker/")
time.sleep(2)
cookie=driver.find_element(By.ID,"bigCookie")
count = driver.find_element(By.ID,"cookies")

def find_product():
    try:
        total = int(count.text.split(" ")[0].replace(",",""))
        upgrades = driver.find_element(By.ID,"upgrades").find_elements(By.CSS_SELECTOR,".crate.upgrade.enabled")
        for upgrade in reversed(upgrades):
            return upgrade
        products = driver.find_element(By.ID,"products").find_elements(By.CSS_SELECTOR,".product.unlocked.enabled .content")    
        for product in reversed(products):
            print(product.find_element(By.CLASS_NAME,"title").text)
            price = int(product.find_element(By.CLASS_NAME,"price").text.replace(",",""))
            print(f"{total} {price}")
            if int(price) < int(total):
                return product
    except Exception as e:
        print(e)
    return None


while time.time() < t_final:
    print("Clicking...")
    while time.time() < t_end:
        cookie.click()
    print("Finished clicking")
    print("Looking through products")
    to_buy = find_product()
    while to_buy:
        try:
            to_buy.click()
            print("Bought")
        except Exception as e:
            print(e)
            break
        to_buy = find_product()
    print("Finished buying")
    t_end = t_end + 5

driver.quit()
