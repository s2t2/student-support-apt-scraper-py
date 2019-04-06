
# adapted from: https://splinter.readthedocs.io/en/latest/
from splinter import Browser

#from bs4 import BeautifulSoup



#browser = Browser(driver_name="chrome") #> selenium.common.exceptions.WebDriverException: Message: Service chromedriver unexpectedly exited. Status code was: 127

with Browser() as browser:
    print(type(browser))

    breakpoint()

    URL = "https://www.avaloncommunities.com/virginia/arlington-apartments/avalon-ballston-square/floor-plans"
    browser.visit(URL)
