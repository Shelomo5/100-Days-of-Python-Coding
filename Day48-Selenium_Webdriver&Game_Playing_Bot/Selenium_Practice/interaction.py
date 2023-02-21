from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

URL= "https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/"

# file path where driver is located on computer
chrome_driver_path = Service("C:/Users/shelo/UDEMY/Installed_Software/chromedriver_win32/chromedriver.exe")

# instantiate chrome browser(object) to drive and keeps chrome screen open, time.sleep(10)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(), options=options)

# Opens up new browser window with specified url
driver.get(URL)

# scrape time and event elements using css selector
# articles_num = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# alternative way
# articles_num = driver.find_element(By.CSS_SELECTOR, '#articlecount a')
# print(articles_num.text)

# clicks on element
# articles_num.click()

# free encyclopedia is hyperlink text on url page and driver clicks on it
# all_portals = driver.find_element(By.LINK_TEXT, "encyclopedia")
# all_portals.click()

# # "search" is name of the element to get hold of
# search = driver.find_element(By.NAME, "search")
# # keys from the keyboard you want to send to search element, so it will type Python
# # Keys class replicates presing a key
# search.send_keys("Python"+Keys.ENTER)

search = driver.find_element(By.NAME, "fName")
search.send_keys("Shelomo")
search = driver.find_element(By.NAME, "lName")
search.send_keys("Bichindaritz")
search = driver.find_element(By.NAME, "email")
search.send_keys("shelomo@att.net")

submit = driver.find_element(By.CSS_SELECTOR, "form button")
submit.click()



