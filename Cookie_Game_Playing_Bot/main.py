from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import os

URL = "http://orteil.dashnet.org/experiments/cookie/"

# file path where driver is located on computer
chrome_driver_path = Service(os.environ["chrome_driver_path"])

# instantiate chrome browser(object) to drive and keeps chrome screen open, time.sleep(10)
driver = webdriver.Chrome(service=Service())

# Opens up new browser window with specified url
driver.get(URL)
# Finds cookie element
cookie = driver.find_element(By.ID, "cookie")

# selector finds elements in right-hand of pane which contain all upgrade items, hashtag for id
pane_upgrades = driver.find_elements(By.CSS_SELECTOR, '#store div')
# retrieve attributes (text of upgrade name) of id element via list comprehension
name_upgrade = [upgrade.get_attribute("id") for upgrade in pane_upgrades]

# time.time() (time is seconds since epoch, start of time)
# used to measure the elapsed wall-clock time between two points

# time check is the current time after 5 sec have elapsed
time_check = time.time() + 5
# bot_pause is current time after 5 min have elapsed
bot_pause = time.time() + (60 * 5)
# equals 5.0 sec

playing = True
while playing:
    # click cookie repeatedly
    cookie.click()
    # if more than 5 sec have elapsed since playing
    if time.time() > time_check:
        # list created where prices will be stored
        pane_prices = []
        # find price for each right pane upgrades, the <b> tags
        prices = driver.find_elements(By.CSS_SELECTOR, "#store div b")

        # iterating over prices elements
        for price in prices:
            # for each element get text
            price_text = price.text
            # convert each price to an int and clean data and append to list
            if price_text != "":
                price_int = int(price_text.split("-")[1].strip().replace(",", ""))
                pane_prices.append(price_int)

        # dictionary to store price values and text name of upgrades
        upgrades_storage = {}
        # for each index number in pane prices
        for n in range(len(pane_prices)):
            # the pane price is associated with its name by associating both lists
            upgrades_storage[pane_prices[n]] = name_upgrade[n]

        # Find cookie total element and remove comma from the number
        cookie_total = driver.find_elements(By.ID, value="money")[0].text
        if "," in cookie_total:
            cookie_total = cookie_total.replace(",", "")
        cookie_number = int(cookie_total)

        affordable_upgrades = {}
        # .items() returns a list with key value pairs as tuples and hence
        # allows us to iterate key value pairs in dictionary upgrades_storage
        for price, upgrade in upgrades_storage.items():
            # if we have enough cookies
            if cookie_number > price:
                # add key value pair (price: upgrade) to affordable_upgrades
                affordable_upgrades[price] = upgrade

        # max() returns largest key (price) within dictionary
        largest_price = max(affordable_upgrades)
        # finding pane upgrade name(value) associated with largest key/price
        upgrade_name_purchasing = affordable_upgrades[largest_price]
        # find element whose name corresponds to upgrade in right pane and click it
        driver.find_element(By.ID, f"{upgrade_name_purchasing}").click()
        # add 5 sec till next time check
        time_check = time.time() + 5

        # after 5 min have elapsed find element cookies/second and print it
        if time.time() > bot_pause:
            cookies_per_second = driver.find_element(By.ID, f"cps").text
            print(f"cookies/second:{cookies_per_second}")
            break

