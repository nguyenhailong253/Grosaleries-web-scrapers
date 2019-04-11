from bs4 import BeautifulSoup as soup
from selenium import webdriver
from urllib.request import urlopen
from time import sleep
import json

def scrapping(container_soup):
    
    containers = container_soup
    print('Total items in this page: ' + str(len(containers)))
    print('')
    
    arr = []
    for container in containers:
        # get the product name
        product_name = container.find('h3', {'class':'shelfProductTile-description'}).text.strip()
        # set the supermarket name to woolies
        supermarket_name = 'Woolsworth'
        # initial product is available
        availability = True

        # check price and availability of each item
        if(container.find('div', {'class': 'shelfProductTile-cupPrice'})):
            price = container.find('div', {'class': 'shelfProductTile-cupPrice'}).text.strip()
        elif(container.find('span', {'class':'price-dollars'})):
            price_dollar = container.find('span',{'class':'price-dollars'})
            price_cent = container.find('span', {'class': 'price-cents'})
            price = '$' + price_dollar.text + '.' + price_cent.text
        else:
            price = 'Unavailable at the momment'
            availability = False

        obj = {
            "supermarket_name": supermarket_name,
            "product_name": product_name,
            "price": price,
            "availability": availability
        }

        #return all the items in the page
        arr.append(obj)
    return arr, len(containers)

# adding webdriver options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=r'C:/Users/Ultabook/Downloads/chromedriver_win32/chromedriver.exe',options=options)

# scrapping woolies vegetables section
arr = [] #used to store every object
n_items = 1
i = 1

while(n_items != 0):
    url = 'https://www.woolworths.com.au/shop/browse/fruit-veg/vegetables?pageNumber=' + str(i)
    print('page ' + str(i) + ": " + url)
    driver.get(url)
    sleep(10)
    html = driver.page_source
    page_soup = soup(html, 'html.parser')
    
    container_soup = page_soup.findAll('div', {'class': 'shelfProductTile-information'})
    arrSinglePage, n_items = scrapping(container_soup)
    for obj in arrSinglePage:
        arr.append(obj)
    i = i + 1

# scrapping woolies fruit section
n_items = 1
i = 1
while(n_items != 0):
    url = 'https://www.woolworths.com.au/shop/browse/fruit-veg/fruit?pageNumber=' + str(i)
    print('page ' + str(i) + ": " + url)
    driver.get(url)
    sleep(10)
    html = driver.page_source
    page_soup = soup(html, 'html.parser')
    
    container_soup = page_soup.findAll('div', {'class': 'shelfProductTile-information'})
    arrSinglePage, n_items = scrapping(container_soup)
    for obj in arrSinglePage:
        arr.append(obj)
    i = i + 1

# scrapping woolies meat section
n_items = 1
i = 1

while(n_items != 0):
    url = 'https://www.woolworths.com.au/shop/browse/meat-seafood-deli/meat?pageNumber=' + str(i)
    print('page ' + str(i) + ": " + url)
    driver.get(url)
    sleep(10)
    html = driver.page_source
    page_soup = soup(html, 'html.parser')
    
    container_soup = page_soup.findAll('div', {'class': 'shelfProductTile-information'})
    arrSinglePage, n_items = scrapping(container_soup)
    for obj in arrSinglePage:
        arr.append(obj)
    i = i + 1

# write a json file on all items    
with open('wooliesData.json', 'w') as outfile:
    json.dump(arr, outfile)

print(len(arr))
