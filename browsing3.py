
import requests
from bs4 import BeautifulSoup

URL = "https://www.avaloncommunities.com/virginia/arlington-apartments/avalon-ballston-square/floor-plans"

# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent#Chrome_UA_string
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"

headers = {'User-Agent': user_agent}

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.content, "html.parser")

print("SOUP:", type(soup))

div = soup.find("div", id="floor-plan-type")

print(div)
