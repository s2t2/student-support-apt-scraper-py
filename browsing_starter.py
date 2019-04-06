# adapted from: https://selenium-python.readthedocs.io/waits.html

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

URL = "https://www.avaloncommunities.com/virginia/arlington-apartments/avalon-ballston-square/floor-plans"

driver = webdriver.Chrome("/usr/local/bin/chromedriver") # location where chromedriver is installed

driver.get(URL)

try:
    #div = driver.find_element_by_id("floor-plan-listing") #> selenium.common.exceptions.NoSuchElementException: Message: no such element: Unable to locate element: {"method":"id","selector":"floor-plan-listing"}
    listings_appear = EC.presence_of_element_located((By.ID, "floor-plan-listing"))
    wait_duration = 3 # seconds
    div = WebDriverWait(driver, wait_duration).until(listings_appear)
    print("PAGE LOADED!")
except TimeoutException:
    print("TIME OUT!")
finally:

    soup = BeautifulSoup(driver.page_source, "html.parser")

    #one_bedrooms = soup.find("div", id="bedrooms-1")
    #print(one_bedrooms)
    #breakpoint()

    one_br_layouts = soup.find("div", id="bedrooms-1").findAll("div", "row")
    for layout in one_br_layouts:
        print(layout)
        print("-----------")
        #breakpoint()




    driver.quit()
