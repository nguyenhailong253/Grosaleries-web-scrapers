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
        product_name = container.find(
            'div', {'class': 'box--description--header'}).text.strip()

        # initial product is available
        availability = True

        # get the date and time of the scrapping time
        date_now = datetime.datetime.now()

        # set initial price to NA
        price = "NA"
        pic = None

        if (container.find('span', {'class': 'box--baseprice'})):
            price = container.find('span', {'class': 'box--baseprice'}).text.strip()
        elif (container.find('span', {'class': 'box--value'})):
            dollar_value = container.find('span', {'class': 'box--value'}).text.strip()
            cent_value = container.find('span', {'class': 'box--decimal'}).text.strip()
            price = dollar_value + cent_value

        if (container.find('div', {'class': 'box--image-container'})):
            tmp = container.find('div', {'class': 'box--image-container'})
            pic = tmp.img['src']

        obj = {
            "name": product_name,
            "price": price,
            "availability": availability,
            "datetime": date_now,
            "category": category,
            "pic": pic
        }

        # return all the items in the page
        arr.append(obj)
    return arr, len(containers)

# convert datetime format to fit json
def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
