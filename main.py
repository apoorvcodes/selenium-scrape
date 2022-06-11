#Script for AT&T

# Import libs and set working dir
import os
os.getcwd()
# set your working directory
os.chdir('C:\\Users\\ACER\\Downloads\\WebScrape')

import time
from re import search
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By

# Get Driver
drvPath = "C:\\Users\\ACER\\Downloads\\WebScrape\\chromedriver_win32\\chromedriver.exe"
browser= webdriver.Chrome(drvPath)

# Open Link
browser.get("https://www.att.com/buy/phones/")

timeout = 30
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, "_2rMgP")))
except TimeoutException:
    browser.quit()

SCROLL_PAUSE_TIME = 1

# Get scroll height
last_height = browser.execute_script("return document.body.scrollHeight")

# Load entire page
while True:
    # Scroll down to bottom
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
    new_height = browser.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


# Get all the links
elements = browser.find_elements(By.CSS_SELECTOR,
"div._2rMgP a")

#Loop through all the links and extract product specific links
a_elements = []
for elms in elements:
    lnk=elms.get_attribute("href")
    if search(str('https://www.att.com/buy/phones/'), str(lnk)) and search(str('.html'), str(lnk)):
        a_elements.append(lnk)

# Verify Links
print (a_elements)
len(a_elements)

# Loop for getting individual product information and creating dataframe

for product in a_elements:
    browser.get(str(product))