from selenium import webdriver
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

GYM_URL = "https://appbrewery.github.io/gym/"
ACCOUNT_PASSWORD = "Hdf44^%$#f32h#@$f"
ACCOUNT_EMAIL = "h.urreyan@gmail.com"

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_option.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_option)
driver.get(GYM_URL)

ask = driver.find_element(by=By.ID, value="login-button")
ask.click()

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, "email-input")))

click_email = driver.find_element(by=By.ID,value="email-input")
click_password = driver.find_element(by=By.ID,value="password-input")

click_email.send_keys(ACCOUNT_EMAIL)
click_password.send_keys(ACCOUNT_PASSWORD)

click_password.send_keys(Keys.ENTER)

wait = WebDriverWait(driver, 10)
# element = wait.until(EC.presence_of_element_located((By.ID, "welcome-message")))

driver.execute_script("window.scrollBy(0, 7000);")  # scrolls down 300px
element = wait.until(EC.presence_of_element_located((By.ID, "day-title-tue,-nov-11")))
types = ["yoga", "spin", "hiit"]
book_class = driver.find_elements(By.XPATH, "//button[contains(@id, 'book-button-') and contains(@id, '2025-11-11')  and not(@disabled)]")
classes_now = 0
watchlist = 0
for i in book_class:

    try:
        i.click()
        

        if i.text == "Booked":
            classes_now += 1
        elif i.text == "Waitlisted":
            watchlist += 1
        print(f"✅ Booked: class successfully")
    except:
        print(f"No found 🦈")
        continue  # move to next if not found
classes_all = driver.find_elements(By.XPATH, "//button[contains(@id, 'book-button-') and (@disabled)]")
classes_all_count = 0
classes_all_tue = driver.find_elements(By.XPATH, "//button[contains(@id, 'book-button-') and contains(@id, '2025-11-11') and (@disabled)]")
classes_all_count_tue = 0

for i in classes_all:
    classes_all_count += 1
for i in classes_all_tue:
    classes_all_count_tue += 1

print("--- BOOKING SUMMARY ---")

print(f"Classes booked: {classes_now}")
print(f"Waitlists joined: {watchlist}")
print(f"Already booked/waitlisted: {classes_all_count}")
print(f"Total Tuesday 6pm classes processed: {classes_all_count_tue}")


