# adapted from https://codereview.stackexchange.com/questions/177977/scraper-to-deal-with-some-complicated-site-with-ads

from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.common.exceptions import TimeoutException
#from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.avaloncommunities.com/virginia/arlington-apartments/avalon-ballston-square/floor-plans"

# driver = webdriver.Chrome()
#> selenium.common.exceptions.WebDriverException: Message: Service chromedriver unexpectedly exited. Status code was: 127

# after installing chromedriver...
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

driver.get(URL)

#wait = WebDriverWait(driver, 10)
#
#try:
#    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[.='SKIP']"))).click()
#except TimeoutException: pass

driver.find_elements_by_css_selector("#bedrooms-1")

breakpoint()

driver.quit()
