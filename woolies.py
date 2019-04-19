from bs4 import BeautifulSoup as soup
from selenium import webdriver
from urllib.request import urlopen
from time import sleep
import json
import datetime

def scrapping(container_soup, category):
    
    containers = container_soup
    print('Total items in this page: ' + str(len(containers)))
    print('')
    
    arr = []
    
    for container in containers:
        # get the product name
        product_name = container.find('h3', {'class':'shelfProductTile-description'}).text.strip()
        # initial product is available
        availability = True
        # get the date and time of the scrapping time
        date_now = datetime.datetime.now()        

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
            "name": product_name,
            "price": price,
            "availability": availability,
            "datetime": date_now,
            "category": category,
            "pic": None
        }

        #return all the items in the page
        arr.append(obj)
    return arr, len(containers)

# adding webdriver options
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=r'C:/Users/Ultabook/Downloads/chromedriver_win32/chromedriver.exe',options=options)

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
arr = [] #used to store every object

# list of url section 
url_header = ['https://www.woolworths.com.au/shop/browse/fruit-veg/vegetables?pageNumber=',
              'https://www.woolworths.com.au/shop/browse/fruit-veg/fruit?pageNumber=',
              'https://www.woolworths.com.au/shop/browse/meat-seafood-deli/meat?pageNumber='
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
    
        container_soup = page_soup.findAll('div', {'class': 'shelfProductTile-information'})
        if(len(container_soup) != 0):
            category = page_soup.find('h1', {'class': 'tileList-title'}).text.strip()
        arrSinglePage, n_items = scrapping(container_soup, category)
        for obj in arrSinglePage:
            arr.append(obj)
        i = i + 1


# add the products array to the full list
products = {'products': arr}
full_list.append(products)

# convert datetime format to fit json
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

# write a json file on all items    
with open('wooliesData.json', 'w') as outfile:
    json.dump(full_list, outfile, default=myconverter)


print(len(arr))
