# adapted from https://codereview.stackexchange.com/questions/177977/scraper-to-deal-with-some-complicated-site-with-ads
# ... https://stackoverflow.com/questions/26566799/wait-until-page-is-loaded-with-selenium-webdriver-for-python/40037216

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

URL = "https://www.avaloncommunities.com/virginia/arlington-apartments/avalon-ballston-square/floor-plans"

driver = webdriver.Chrome("/usr/local/bin/chromedriver")

driver.get(URL)
#driver.find_elements_by_css_selector("#bedrooms-1")

###wait = WebDriverWait(driver, 10)
###
###wait.until(ec.visibility_of_element_located("floor-plan-listing"))
###
####try:
####    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[.='SKIP']"))).click()
####except TimeoutException: pass

try:
    #
    # WAIT UNTIL CONTENTS ARE LOADED
    #

    delay_seconds = 10
    wait = WebDriverWait(driver, delay_seconds)
    div = wait.until(EC.presence_of_element_located(By.ID, "floor-plan-listing"))
    #div = wait.until(EC.visibility_of_element_located(By.ID, "floor-plan-listing"))

    print("LOADED!")
    print(div)

    #
    # PARSE CONTENTS
    #

    soup = BeautifulSoup(driver.page_source, "html.parser")

    outer_div = soup.find("div", id="floor-plan-type")
    print(outer_div)
    print("-----------------")

    one_bedrooms_div = soup.find("div", id="bedrooms-1")

    print(one_bedrooms_div)
    #breakpoint()

except TimeoutException:
    print("OOPS, TIME OUT!")
except:
    print("OOPS")
    driver.quit()


driver.quit()
