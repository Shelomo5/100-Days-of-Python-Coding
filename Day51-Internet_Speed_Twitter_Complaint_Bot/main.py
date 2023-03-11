from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
import time
import os


PROMISED_DOWNLOAD = 400
PROMISED_UPLOAD = 10
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
USERNAME = os.environ["USERNAME"]

# Selenium page load strategy set not to wait for full page load
caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"


# file path where driver is located on computer
chrome_driver_path = Service(os.environ["chrome_driver_path"])
Speed_Test_URL = "https://www.speedtest.net/"
Twitter_URL = "https://twitter.com/login"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        # instantiate chrome browser(object) to drive and keeps chrome screen open
        self.driver = webdriver.Chrome(service=Service(), desired_capabilities=caps)
        # Download speed attribute
        self.download = 0
        # Upload speed attribute
        self.upload = 0

    def get_internet_speed(self):
        # To ensure window is full size as that can change html
        self.driver.maximize_window()

        # Opens up new browser window with specified url
        self.driver.get(Speed_Test_URL)
        # time WebDriver waits when searching for element if not immediately present
        time.sleep(3)
        # finds starting button and clicks on it
        start_button = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]")
        start_button.click()
        # sleep to wait for the results
        WebDriverWait(self.driver, 120).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "result-label"))
        )

        self.download = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        self.upload = self.driver.find_element(By.XPATH,  "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        print(f"download: {self.download} Mbps upload: {self.upload} Mbps")


    def tweet_at_provider(self):
        self.driver.implicitly_wait(10)

        # Maximizes size of window
        self.driver.maximize_window()

        # Opens up twitter login
        self.driver.get(Twitter_URL)
        self.driver.implicitly_wait(10)
        time.sleep(5)

        # Enter email
        email = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email.send_keys(TWITTER_EMAIL)
        self.driver.implicitly_wait(6)
        time.sleep(4)

        # Find and click next
        next = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span")
        next.click()
        self.driver.implicitly_wait(8)
        time.sleep(2)
        # If twitter requires username for verification provide it but if not needed pass
        try:
            phone = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
            phone.send_keys(USERNAME)
            time.sleep(3)
            phone.send_keys(Keys.ENTER)
            time.sleep(5)
        except NoSuchElementException or TimeoutException:
            pass
        self.driver.implicitly_wait(10)
        time.sleep(3)

        # Enter Password
        password = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password.send_keys(TWITTER_PASSWORD)
        self.driver.implicitly_wait(9)

        # Find and click login button
        log_in = self.driver.find_element(By.XPATH,"/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span")
        log_in.click()
        self.driver.implicitly_wait(10)
        time.sleep(5)

        # Insert Tweet in text box
        tweet = self.driver.find_element(By.XPATH,"//div[contains(@aria-label, 'Tweet text')]")
        self.driver.implicitly_wait(10)
        tweet_text = f"Hi Comcast, why is my internet speed {self.download} Mbps download/{self.upload} Mbps upload when I pay for {PROMISED_DOWNLOAD} Mbps download/{PROMISED_UPLOAD} Mbps upload?"
        tweet.send_keys(tweet_text)
        self.driver.implicitly_wait(10)
        time.sleep(3)

        # Send tweet
        send_tweet = self.driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
        send_tweet.click()
        time.sleep(10)

# initiate class object
bot = InternetSpeedTwitterBot(chrome_driver_path)
# Method to get internet speed
bot.get_internet_speed()
time.sleep(5)
# Method to tweet internet speed
bot.tweet_at_provider()