# adapted from: https://selenium-python.readthedocs.io/waits.html

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

URL = "https://www.avaloncommunities.com/virginia/arlington-apartments/avalon-ballston-square/floor-plans"

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

#driver.implicitly_wait(10) # seconds

driver.get(URL)

try:
    #div = driver.find_element_by_id("floor-plan-listing") #> selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"id","selector":"floor-plan-listing"}
    div = WebDriverWait(driver, 6).until(
        EC.presence_of_element_located((By.ID, "floor-plan-listing"))
    )
    print("PAGE LOADED")
except TimeoutException:
    print("TIME OUT!")
finally:
    soup = BeautifulSoup(driver.page_source, "html.parser")
    print(soup.find("div", id="floor-plan-type"))
    print("-----------------")
    print(soup.find("div", id="bedrooms-1"))
    print("-----------------")
    driver.quit()
