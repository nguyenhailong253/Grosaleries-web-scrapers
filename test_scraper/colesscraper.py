
import os
import sys
import time
import json
import requests
import pandas as pd
import urllib.request
import codecs
from itertools import cycle
from selenium import webdriver
from bs4 import BeautifulSoup as soup
from requests_html import HTMLSession

HEADERS = {
    'User-agent':
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}


class ColesScraper:
    ''' Scraper for Coles's products '''

    def __init__(self):
        super().__init__()
        self.data = {
            "supermarket_name": "",
            "product_name": "",
            "price": "",
            "availability": "",
        }

        self.driver_path = r'./chromedriver.exe'

    def init_driver(self):
        ''' Initialize web driver '''

        self.options = webdriver.ChromeOptions()
        self.options.add_argument(
            '--user-agent={}'.format(HEADERS))

        self.driver = webdriver.Chrome(
            executable_path=self.driver_path, chrome_options=self.options)

    def scrape_page(self, containers):
        ''' Scraping coles' product's info '''

        arr = []
        for container in containers:
            product_name = container.find(
                'span', {'class': 'product-name'}).get_text()
            supermarket_name = 'Coles'

            if(container.find('div', {'class': 'product-flag'})):
                availability = False
            else:
                availability = True

            if(container.find('span', {'class': 'price-container'})):
                price_dollar = container.find(
                    'span', {'class': 'dollar-value'}).get_text()

                price_cent = container.find(
                    'span', {'class': 'cent-value'}).get_text()

                price = '$' + price_dollar + price_cent
                if(container.find('span', {'class': 'package-size'})):
                    package_size = container.find(
                        'span', {'class': 'package-size'}).get_text()
                    price = price + ' for ' + package_size
            else:
                price = 'Unavailable at the moment'

            obj = {
                "supermarket_name": supermarket_name,
                "product_name": product_name,
                "price": price,
                "availability": availability
            }
            print(obj)
            print("\n")
            arr.append(obj)

        return arr

    def scrape_from_html(self):
        ''' Scrape data from downloaded htmml file '''

        # open HTML file in read only mode
        html = codecs.open("Coles Online.html", 'r', 'utf-8')

        # parse the content
        page_soup = soup(html.read(), 'html.parser')

        # find container div
        container_soup = page_soup.find_all(
            'div', {'class': 'product-main-info'})
        arr = []

        # get list of dict of scraped info
        arrSinglePage = self.scrape_page(container_soup)
        for obj in arrSinglePage:
            arr.append(obj)

        # writing to json file
        with open('colesData.json', 'w') as outfile:
            json.dump(arr, outfile)

    def get_body_html(self):
        ''' Request Coles website 

            NOT WORKING AT THE MOMENT
        '''

        done = False

        while not done:
            try:
                url = 'https://shop.coles.com.au/a/a-vic-metro-vermont-south/everything/browse/fruit-vegetables?pageNumber=1'

                html = urllib.request.urlopen(url)
                text = html.read()
                string = text.decode('utf-8')
                html.close()
                print("this is HTML \n", html)
                print("this is TEXT \n", text)
                print("this is STRING \n", string)

            except Exception as p:
                print(p)
                print(" # ========================================================# ")
                time.sleep(1)


def main():
    scraper = ColesScraper()
    # scraper.get_body_html()
    scraper.scrape_from_html()
    print("Finished scraping Coles")


if __name__ == "__main__":
    main()
