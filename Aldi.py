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
        product_name = container.find('div', {'class':'box--description--header'}).text.strip()
        # initial product is available
        availability = True
        # get the date and time of the scrapping time
        date_now = datetime.datetime.now()        
        
        price = container.find('span', {'class': 'box--baseprice'}).text.strip()

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
    {"name": "Aldi",
    "description": "Aldi Supermarket",
    "url": "https://www.aldi.com.au",
    "added_datetime": None
    }
}
full_list.append(seller)
arr = [] #used to store every object

# list of url section 
url_header = ['https://www.aldi.com.au/en/groceries/super-savers/',
              'https://www.aldi.com.au/en/groceries/just-organic/',
              'https://www.aldi.com.au/en/groceries/awards/',
              'https://www.aldi.com.au/en/groceries/baby-care/',
              'https://www.aldi.com.au/en/groceries/chocolate/',
              'https://www.aldi.com.au/en/groceries/coffee/',
              'https://www.aldi.com.au/en/groceries/gluten-free/',
              'https://www.aldi.com.au/en/groceries/olive-oils/'']

# scrapping for each section selected in the list
for header in url_header:
    url = header
    print(url)
    driver.get(url)
    sleep(10)
    html = driver.page_source
    page_soup = soup(html, 'html.parser')
    
    container_soup = page_soup.findAll('a', {'title': 'to product detail'})
    if(len(container_soup) != 0):
        category = page_soup.findAll('li', {'property': 'itemListElement'})[2].text.strip()
        print(category)
    arrSinglePage, n_items = scrapping(container_soup, category)
    for obj in arrSinglePage:
        arr.append(obj)

# add the products array to the full list
products = {'products': arr}
full_list.append(products)

# convert datetime format to fit json
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

# write a json file on all items    
with open('aldiData.json', 'w') as outfile:
    json.dump(full_list, outfile, default=myconverter)


print(len(arr))
