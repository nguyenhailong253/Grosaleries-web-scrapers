from bs4 import BeautifulSoup as soup
from selenium import webdriver
from urllib.request import urlopen
from time import sleep
from woolieshelper import *
import json
import datetime

# adding webdriver options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(
    executable_path=r'../../utils/chromedriver.exe', options=options)

# contain full list details for woolies
full_list = []
seller = {
    "seller":
    {"name": "Woolsworth",
     "description": "Woolsworth Supermarket",
     "url": "https://www.woolsworth.com.au",
     "added_datetime": None
     }
}
full_list.append(seller)
arr = []  # used to store every object

# list of url section
url_header = ['https://www.woolworths.com.au/shop/browse/fruit-veg?pageNumber=',
              'https://www.woolworths.com.au/shop/browse/meat-seafood-deli?pageNumber=',
              'https://www.woolworths.com.au/shop/browse/bakery?pageNumber=',
              'https://www.woolworths.com.au/shop/browse/dairy-eggs-fridge?pageNumber=',
              'https://www.woolworths.com.au/shop/browse/pantry?pageNumber=',
              'https://www.woolworths.com.au/shop/browse/freezer?pageNumber=',
              'https://www.woolworths.com.au/shop/browse/drinks?pageNumber=',
              'https://www.woolworths.com.au/shop/browse/liquor?pageNumber='
              ]

# scrapping for each section selected in the list
for header in url_header:
    n_items = 1
    i = 1

    while(n_items != 0):
        url = header + str(i)
        print('page ' + str(i) + ": " + url)
        driver.get(url)
        sleep(10)
        html = driver.page_source
        page_soup = soup(html, 'html.parser')

        container_soup = page_soup.findAll(
            'div', {'class': 'shelfProductTile-information'})
        if(len(container_soup) != 0):
            category = page_soup.find(
                'h1', {'class': 'tileList-title'}).text.strip()
        arrSinglePage, n_items = scrapping(container_soup, category)
        for obj in arrSinglePage:
            arr.append(obj)
        i = i + 1

# add the products array to the full list
products = {'products': arr}
full_list.append(products)

# write a json file on all items
with open('wooliesData.json', 'w') as outfile:
    json.dump(full_list, outfile, default=myconverter)

print(len(arr))
