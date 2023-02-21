from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

URL= "https://www.python.org/"

# file path where driver is located on computer
chrome_driver_path = Service("C:/Users/shelo/UDEMY/Installed_Software/chromedriver_win32/chromedriver.exe")

# instantiate chrome browser(object) to drive
driver = webdriver.Chrome(service=chrome_driver_path)

# Opens up new browser window with specified url
driver.get(URL)

# scrape time and event elements using css selector
time_element = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_element = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")

# creating a nested dictionary of time and event key value pairs
events = {

    item:{
        "time": time_element[item].text,
        "name": event_element[item].text
        }
    for item in range(len(event_element))
}
print(events)




# closes browser
driver.quit()