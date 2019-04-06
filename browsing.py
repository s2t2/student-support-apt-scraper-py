
# adapted from: https://splinter.readthedocs.io/en/latest/
from splinter import Browser

#from bs4 import BeautifulSoup

browser = Browser()

# > selenium.common.exceptions.WebDriverException: Message: newSession

browser = Browser(driver_name="chrome")
#> selenium.common.exceptions.WebDriverException: Message: Service chromedriver unexpectedly exited. Status code was: 127

print(type(browser))

URL = "https://www.avaloncommunities.com/virginia/arlington-apartments/avalon-ballston-square/floor-plans"
browser.visit(URL)

breakpoint()
