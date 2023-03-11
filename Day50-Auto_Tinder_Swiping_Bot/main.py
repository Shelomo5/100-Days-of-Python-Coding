from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
import os

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

Tinder_Url= "https://tinder.com/"

# file path where driver is located on computer
chrome_driver_path = Service(os.environ["chrome_driver_path"])

# instantiate chrome browser(object) to drive and keeps chrome screen open
driver = webdriver.Chrome(service=Service())

# To ensure window is full size as that can change html
driver.maximize_window()

# Opens up new browser window with specified url
driver.get(Tinder_Url)
# time WebDriver waits when searching for element if not immediately present
driver.implicitly_wait(10)

# clicks on login button
login_button = driver.find_element(By.LINK_TEXT, "Log in")
time.sleep(3)
login_button.click()
time.sleep(5)

# click more options button
More_Options_Button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/button")
More_Options_Button.click()
time.sleep(3)

# click facebook login button
Facebook_Login = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/div/div[3]/span/div[3]/button/div[2]/div[2]/div/div")
Facebook_Login.click()
time.sleep(3)

# We have to switch the popup window to be the main window for Selenium to work
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)
print(driver.window_handles)

# Enter email
email = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[1]/div/input")
email.send_keys(EMAIL)
time.sleep(3)

# Enter password
password = driver.find_element(By.XPATH, "/html/body/div/div[2]/div[1]/form/div/div[2]/div/input")
password.send_keys(PASSWORD)

# Press enter
password.send_keys(Keys.ENTER)
time.sleep(5)

# Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(3)

# Click on don't allow Location button
location = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]").click()
time.sleep(3)

# Click on not interested in notifications
notification = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[2]/div[2]/div[2]").click()
time.sleep(3)

# Click on accept cookies
Cookies = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]").click()
time.sleep(3)
# //*[@id='c-60880778']/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button

# find dislike button
dislike = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[2]/button")
for n in range(0,5):
    time.sleep(2)
    try:
        # click on dislike button
        dislike.click()
    # exception when the matches in area haven't loaded yet
    except NoSuchElementException:
        time.sleep(2)

# exit driver
driver.quit()