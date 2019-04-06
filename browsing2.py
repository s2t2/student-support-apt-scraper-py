# adapted from:
# ... https://github.com/python-mechanize/mechanize
# ... https://mechanize.readthedocs.io/en/latest/
# ...

import re
import mechanize

URL = "https://www.avaloncommunities.com/virginia/arlington-apartments/avalon-ballston-square"

browser = mechanize.Browser()

#browser.set_handle_robots(False)

browser.open(URL)
# browser.geturl()
# browser.response().read()


breakpoint()
