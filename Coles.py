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
        product_name = container.find('h3', {'class':'product-title'})
        supermarket_name = 'Coles'

        if(container.find('div', {'class':'product-flag'})):
            availability = False
        else:
            availability = True

        if(container.find('span', {'class':'dollar-val'})):
            price_dollar = container.find('span',{'class':'dollar-val'})
            price_cent = container.find('span', {'class': 'cent-val'})
            price = '$' + price_dollar.text + '.' + price_cent.text
            if(container.find('span', {'class': 'package-size'})):
                package_size = container.find('span', {'class':'package-size'})
                price = price + ' for ' + package_size
            if(container.find('span', {'class':'package-price'})):
                package_price = container.find('span', {'class':'package-price'})
                price = price + '/' + package_price
        else:
            price = 'Unavailable at the moment'

        obj = {
            "supermarket_name": supermarket_name,
            "product_name": product_name,
            "price": price,
            "availability": availability
        }
        
        arr.append(obj)
    return arr

path_khai = r'C:/Users/Ultabook/Downloads/chromedriver_win32/chromedriver.exe'
path_Ben = r'C:\Users\ben-p\chromedriver.exe' 

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=path_khai,options=options)
arr = []

for i in range(1,8): #number of pages plus one
    url = 'https://shop.coles.com.au/a/a-vic-metro-vermont-south/everything/browse/fruit-vegetables?pageNumber=' + str(i)
    print('page ' + str(i) + ": " + url)
    driver.get(url)
    sleep(10)
    html = driver.page_source
    page_soup = soup(html, 'html.parser')
    
    container_soup = page_soup.findAll('div', {'class': 'product-main-info'})
    arrSinglePage = scrapping(container_soup)
    for obj in arrSinglePage:
        arr.append(obj)
        
for i in range(1,4):
    url = 'https://shop.coles.com.au/a/a-vic-metro-vermont-south/everything/browse/fruit-vegetables?pageNumber=' + str(i)
    print('page ' + str(i) + ": " + url)
    driver.get(url)
    sleep(10)
    html = driver.page_source
    page_soup = soup(html, 'html.parser')
    
    container_soup = page_soup.findAll('div', {'class': 'product-main-info'})
    arrSinglePage = scrapping(container_soup)
    for obj in arrSinglePage:
        arr.append(obj)    
    
with open('colesData.json', 'w') as outfile:
    json.dump(arr, outfile)

print(len(arr))
