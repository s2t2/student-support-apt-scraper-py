# adapted from: https://selenium-python.readthedocs.io/waits.html

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

URL = "https://www.avaloncommunities.com/virginia/arlington-apartments/avalon-ballston-square/floor-plans"

#driver = webdriver.Chrome("/usr/local/bin/chromedriver") # location where chromedriver is installed

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

        #print(layout)
        #print("-----------")
        #breakpoint()

        h4 = layout.find("h4").text #> '1 bedroom, 1 bath (400 sq ft) '
        print("LAYOUT: ", h4.upper())

        #h5 = layout.find("h5").text #> 'Finish Package I'
        #print(h5.upper())

        package_names = [h5.text for h5 in layout.findAll("h5")]
        print("PACKAGES:", package_names)

        #table = layout.find("table", "table")
        #header_row = table.find("thead").findAll("th")
        #print(header_row) #> [<th> </th>, <th>Apartment</th>, <th>Available</th>, <th>Starting At</th>, <th></th>]
        #print(header_row[3].text) #> 'Starting At'
#
        #rows = table.find("tbody").findAll("tr")
        #for row in rows:
        #    #print(row)
        #    values = row.findAll("td")
        #    print(values)
        #    print("---")

        #tables = layout.findAll("table", "table")
        #for table in tables:
#
        #    header_row = table.find("thead").findAll("th")
        #    #print(header_row) #> [<th> </th>, <th>Apartment</th>, <th>Available</th>, <th>Starting At</th>, <th></th>]
        #    #print(header_row[3].text) #> 'Starting At'
#
        #    rows = table.find("tbody").findAll("tr")
        #    for row in rows:
        #        #print(row)
        #        values = row.findAll("td")
        #        print(values)
        #        print("---")
#
        #    print("------")
#
        #print("----------------")

    driver.quit()
