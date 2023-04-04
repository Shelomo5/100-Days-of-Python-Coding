import requests
from bs4 import BeautifulSoup
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import os
import time


# file path where driver is located on computer
chrome_driver_path = Service(os.environ["chrome_driver_path"])
Google_Form_URL = "https://docs.google.com/forms/d/e/1FAIpQLSccD-Y6aoIZf08M_OWMUW1V8YZnbhOe-x7NT9Fttnf8SrkWSA/viewform?usp=sf_link"
Zillow_URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

# Headers passed into the request
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
    "Accept-Language": "en-US"
}

# get hold of data from Zillow URL
response = requests.get(url=Zillow_URL, headers=headers)
# raw text
listing_data = response.text


# instantiating class and passing in data, soup is object
# specifying language of parser for file
soup = BeautifulSoup(listing_data, "html.parser")
# soup returns a list containing a JSON with Zillow housing information
data = soup.find_all("script", attrs={"type": "application/json"})

# converts output to text and grabs second element in list
zillow_data = data[1].text
# using .replace method to edit data
zillow_data = zillow_data.replace("<!--", "")
zillow_data = zillow_data.replace("-->", "")
# converts JSON data into Python dictionary
zillow_data = json.loads(zillow_data)
# accessing relevant information within dict
relevant_data = (zillow_data["cat1"]["searchResults"]["listResults"])
# print(relevant_data)

# creating lists to contain relevant data
links_list = []
prices_list = []
addresses_list = []

# iterating through relevant_data and appending links, prices, and addresses to respective list
for relevant in relevant_data:
    link = relevant["detailUrl"]
    # if statement because some links don't contain "https://www.zillow.com"
    if "https://www.zillow.com" in link:
        links_list.append(link)
    else:
        links_list.append("https://www.zillow.com" + link)
    try:
        prices_list.append(relevant["price"])
        addresses_list.append(relevant["address"])
    # exception when the key for the price is different because there are multiple prices
    except KeyError:
        prices_list.append(relevant['units'][0]["price"])
        addresses_list.append(relevant["address"])
# print(prices_list)
# print(addresses_list)


# --------------------------Filling out google form using data pulled from zillow--------------------------------

# file path where driver is located on computer
chrome_driver_path = Service(os.environ["chrome_driver_path"])

# instantiate chrome browser(object) to drive and keeps chrome screen open
driver = webdriver.Chrome(service=Service())

for n in range(len(relevant_data)):
    # To ensure window is full size as that can change html
    driver.maximize_window()
    # Opens up new browser window with specified url
    driver.get(Google_Form_URL)
    time.sleep(2)

    # Finding each element
    address_input = driver.find_elements(By.CSS_SELECTOR, 'div.Xb9hP input')[0]
    price_input = driver.find_elements(By.CSS_SELECTOR, 'div.Xb9hP input')[1]
    link_input = driver.find_elements(By.CSS_SELECTOR, 'div.Xb9hP input')[2]
    send_button = driver.find_element(By.CSS_SELECTOR, 'span.l4V7wb')

    # Input address, price, link and sending it to sheets
    address_input.send_keys(addresses_list[n])
    # time.sleep(.3)
    price_input.send_keys(prices_list[n])
    # time.sleep(.3)
    link_input.send_keys(links_list[n])
    # time.sleep(.3)
    send_button.click()
    # time.sleep(.3)



