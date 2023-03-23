from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]
USERNAME = os.environ["USERNAME"]

JOB_URL = ("https://www.linkedin.com/jobs/search/?currentJobId=3531674919&f_LF=f_AL&geoId=104116203&keywords=python%20developer&location=Seattle%2C%20Washington%2C%20United%20States&refresh=true&start=100")

# file path where driver is located on computer
chrome_driver_path = Service(os.environ["chrome_driver_path"])

# instantiate chrome browser(object) to drive and keeps chrome screen open
driver = webdriver.Chrome(service=Service())

# To ensure window is full size
driver.maximize_window()

# Opens up new browser window with specified url
driver.get(JOB_URL)
driver.implicitly_wait(10)

# Clicks on sign-in button
sign_in = driver.find_element(By.XPATH, "/html/body/div[3]/a[1]")
sign_in.click()
driver.implicitly_wait(10)
time.sleep(2)

# enters email in the right field
search = driver.find_element(By.NAME, "session_key")
search.send_keys(EMAIL)

# enters password in the right field
search = driver.find_element(By.NAME, "session_password")
search.send_keys(PASSWORD)

# clicks on different sign-in button to submit email and password
# time sleep allows time for page to load
sign_in_2 = driver.find_element(By.XPATH, "//*[@id='organic-div']/form/div[3]/button")
sign_in_2.click()
driver.implicitly_wait(10)
time.sleep(3)

# Opens up new browser window with specified url, linkedin goes to default page after logging in
driver.get(JOB_URL)
driver.implicitly_wait(10)

# Find each job listing element
jobs_list = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")

# Iterate through each job
for job in jobs_list:
    # scrolls down so we can click on job
    actions = ActionChains(driver)
    actions.move_to_element(job).perform()
    print("selected")
    # Click on job
    job.click()
    time.sleep(2)

    try:
        # Find and click on easy apply element
        easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
        easy_apply.click()
        time.sleep(2)

        # Find element on bottom right of screen which could be "Next" or "Submit application"
        check_button = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary span")
        # If button isn't next
        if check_button.text != "Next":
            try:
                driver.implicitly_wait(5)
                # clicks on follow button to unfollow
                unfollow = driver.find_element(By.CSS_SELECTOR, "div form footer div label")
                unfollow.click()
                print("button unclicked")
                time.sleep(2)
                driver.implicitly_wait(10)
            except NoSuchElementException or ElementClickInterceptedException:
                pass
                driver.implicitly_wait(10)
                time.sleep(2)

            # click Submit application button
            submit = driver.find_element(By.CSS_SELECTOR, ".artdeco-button--primary")
            submit.click()
            print("Application to job successful!")
            time.sleep(2)

            # Once application completed, close the pop-up window.
            close_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_button.click()
            time.sleep(2)

        else:
            print("Job skipped, had too many steps.")
            close = driver.find_element(By.CSS_SELECTOR, ".artdeco-modal__dismiss")
            close.click()
            time.sleep(2)
            discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn")
            discard_button.click()
            time.sleep(2)

    # custom exception when easy apply button element can't be found
    except NoSuchElementException:
        print("Job skipped, no application button")
        continue
# exit driver
driver.quit()