from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
import os

Instagram_URL = "https://www.instagram.com/accounts/login/"
# Url to profile
Instagram_Profile = "k.mbappe/"


chrome_driver_path = Service(os.environ["chrome_driver_path"])
INSTAGRAM_EMAIL = os.environ["INSTAGRAM_EMAIL"]
INSTAGRAM_PASSWORD = os.environ["INSTAGRAM_PASSWORD"]

# creating class to follow Instagram individuals
class InstaFollower:
    def __init__(self, driver_path):
        # instantiate chrome browser(object) to drive and keeps chrome screen open
        self.driver = webdriver.Chrome(service=Service())
    def login(self):
        # Maximizes size of window
        self.driver.maximize_window()

        # Opens up instagram login
        self.driver.get(Instagram_URL)
        self.driver.implicitly_wait(10)
        time.sleep(5)

        # puts email in
        email = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[1]/div/label/input")
        email.send_keys(INSTAGRAM_EMAIL)
        self.driver.implicitly_wait(10)

        # puts password in
        password = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[2]/div/label/input")
        password.send_keys(INSTAGRAM_PASSWORD)
        self.driver.implicitly_wait(10)

        # clicks on login button
        login = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[3]/button/div")
        login.click()
        self.driver.implicitly_wait(10)

        try:
            # clicks on not now button if it's present
            not_now = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/button")
            not_now.click()
            self.driver.implicitly_wait(10)
        except NoSuchElementException or TimeoutException:
            pass
            self.driver.implicitly_wait(10)
            time.sleep(3)

        try:
            # clicks on turn off notifications button if it's present
            notifications_but = self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
            notifications_but.click()
            self.driver.implicitly_wait(10)
        except NoSuchElementException or TimeoutException:
            pass
            self.driver.implicitly_wait(10)
            time.sleep(3)

    # method scrolls down so all followers can be seen and later clicked on
    def find_followers(self):
        # Maximizes size of window
        self.driver.maximize_window()

        # Opens up instagram login
        self.driver.get("https://www.instagram.com/"+Instagram_Profile)
        self.driver.implicitly_wait(10)
        time.sleep(5)

        # Clicks on Followers button
        followers_button = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a")
        followers_button.click()
        self.driver.implicitly_wait(8)

        # Finds element which contains all follow buttons
        followers_list = self.driver.find_element(By.XPATH, "//div[@class='_aano']")

        for i in range(3):
            # scrolls down so all follow buttons can be seen
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_list)
            self.driver.implicitly_wait(10)
            time.sleep(2)

    # clicks on follow button if it has not be already clicked
    def follow(self):
        follow_btns = self.driver.find_elements(By.CSS_SELECTOR, 'div._aano  button._acan._acap._acas._aj1-')

        for follow in follow_btns:
            # If follow button already clicked
            if follow.text == 'Following' or follow.text == 'Requested':
                print("already clicked")
            else:
                follow.click()
                time.sleep(3)


# Instantiating class object
instagram = InstaFollower(chrome_driver_path)
# Login to instagram
instagram.login()
# Method shows followers
instagram.find_followers()
# Clicks on followers
instagram.follow()

