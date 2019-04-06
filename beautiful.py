#import datetime
#import tkinter as tk
#from tkinter import *
from bs4 import BeautifulSoup
import requests

page_link = 'https://www.avaloncommunities.com/virginia/arlington-apartments/avalon-ballston-square/floor-plans'
page_response = requests.get(page_link, timeout=5)
soup = BeautifulSoup(page_response.content, "html.parser")
print("SOUP:", type(soup))

#textContent = []
#for i in range(0, 20):
#    paragraphs = page_content.find_all("p")[i].text
#    textContent.append(paragraphs)
#
#paragraphs = page_content.find_all("p")[i].text
#specials = soup.findAll("div",{"class": "specials-content row"}) #figure out the right class
#print(specials)

#stuck on class structure

#https://www.youtube.com/watch?v=XQgXKtPSzUI
#https://www.avaloncommunities.com/virginia/arlington-apartments/avalon-ballston-square/apartment/VA559-VA559-001-0215
#https://codeburst.io/web-scraping-101-with-python-beautiful-soup-bb617be1f486
#to capture more user requests/ give them some kind of dropdown











import pprint

pp = pprint.PrettyPrinter(indent=4)

#breakpoint()
#tables = soup.findAll("table")
#
# only table[0] is interesting
#
#<table class="table">
#<tr>
#<td class="model">1 bedroom</td>
#<td>
#<span class="from">From</span><span class="price">$1,737</span>
#</td>
#</tr>
#<tr>
#<td class="model">2 bedrooms</td>
#<td>
#<span class="from">From</span><span class="price">$2,827</span>
#</td>
#</tr>
#<tr>
#<td class="model">Den</td>
#<td>
#<span class="from">From</span><span class="price">$2,505</span>
#</td>
#</tr>
#</table>

table = soup.find("table", "table") # find first "table" element with a class name of "table"
print("TABLE")
print(type(table))
print("---------------------------")
pp.pprint(table.prettify())

breakpoint()

soup.find("section", id="floor-plans")
soup.find("div", id="apartment_results")
soup.find("div", id="floor-plan-type")
# (Pdb) soup.find("div", id="floor-plan-type")
#>
# <div class="tab-content" id="floor-plan-type">
# <!-- dont actually load this beast until we need it. make use of lazyload to see if were here--><img class="lazyload" data-src="/_res/img/pixel.gif" data-src-mobile="/_res/img/pixel.gif" src="data:image/gif;base64,R0lGODlhAQABAPAAAP///wAAACH5BAEAAAAALAAAAAABAAEAAAICRAEAOw=="/>
# <div class="clearfix tab-content" id="bedrooms-1"></div>
# <div class="clearfix tab-content" id="bedrooms-2"></div>
# <div class="clearfix tab-content" id="specials"></div>

# looks like the actual page contents are loaded later via JavaScript, which makes them a lot harder to parse
# would need to use an automated browser solution to request page contents afterwards
