# adapted from: https://selenium-python.readthedocs.io/waits.html

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

URL = "https://www.avaloncommunities.com/virginia/arlington-apartments/avalon-ballston-square/floor-plans"

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

driver.get(URL)

try:
    div = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "floor-plan-listing"))
    )
    print("PAGE LOADED")
    print(div)
except TimeoutException:
    print("OOPS, TIME OUT!")
finally:
    driver.quit()
