# webdriver drives chrome browser and does automated tasks
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

URL="https://www.amazon.com/Copper-Pitcher-Lid-Handcrafted-Hammered/dp/B08LQTQM1D/?_encoding=UTF8&pd_rd_w=DskgO&content-id=amzn1.sym.a5eaa569-8a45-4530-84d2-2dcf8023272a&pf_rd_p=a5eaa569-8a45-4530-84d2-2dcf8023272a&pf_rd_r=9VXTGDNMG5Y4C4X3D08Q&pd_rd_wg=P89DL&pd_rd_r=f1ecb77b-f50a-4b51-b703-ab125f0562d3&ref_=pd_gw_ci_mcx_mi"
# file path where driver is located on computer
chrome_driver_path = Service("C:/Users/shelo/UDEMY/Installed_Software/chromedriver_win32/chromedriver.exe")

# instantiate chrome browser(object) to drive

driver = webdriver.Chrome(service=chrome_driver_path)

# Opens up new browser window with specified url
driver.get(URL)
price = driver.find_element(by=By.CLASS_NAME, value="a-offscreen").get_attribute("textContent")
print(price)

# search_bar = driver.find_element_by_name("q")
# print(search_bar.get_attribute("placeholder"))

# look for anchor tag within this class
# doncumentation_link = driver.find_element(by=By.CSS_SELECTOR(".documentation-widget a")

# x path always works, it locates via path, navigate down html attibutes
# driver.find_element(By.XPATH, 'Xpath')

# you can also search by elements


# closes browser
driver.quit()