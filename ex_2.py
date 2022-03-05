# Exercise 2 - Pawe l Domaga la - Medium

from urllib import request as re
from bs4 import BeautifulSoup as BS
import pandas as pd

# We download the code as before:
url = 'https://www.pythonscraping.com/pages/page3.html'
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')

# Extact Pawe l’s date of birth.
date_of_birth = bs.find("span", {"class": "bday"}).getText()
print(date_of_birth)

# Extract Pawe l’s three occupations.
occupation = bs.find_all('div', {'class': 'hlist hlist-separated'})
for name in occupation:
    print(name.get_text())

# Extract the list of references.
references = bs.find_all('div', {'class': 'mw-references-wrap mw-references-columns'})
for name in references:
    print(name.get_text())
