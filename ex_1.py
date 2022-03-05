# Exercise 1 - Totally Normal Gifts - Easy

from urllib import request as re
from bs4 import BeautifulSoup as BS
import pandas as pd

# We download the code as before:
url = 'https://www.pythonscraping.com/pages/page3.html'
html = re.urlopen(url)
bs = BS(html.read(), 'html.parser')

# Extract bolded parts of the text.
boldText = bs.find_all('span', {'class': 'excitingNote'})
for name in boldText:
    print(name.get_text())

# Extract the last Item Title from the table.
lastTitle = bs.find('tr', {'id': 'gift5'}).td.text
print(lastTitle)

# Extract the footer of the webpage.
footer = bs.find('div', {'id': 'footer'}).getText()
print(footer)
