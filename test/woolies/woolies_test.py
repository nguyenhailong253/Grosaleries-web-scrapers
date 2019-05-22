import unittest
import datetime
from bs4 import BeautifulSoup as soup
from woolieshelper import *

class TestWoolies(unittest.TestCase):

    def test_converter(self):
        obj = datetime.datetime.now()
        actual = myconverter(obj)
        
        self.assertEqual(isinstance(actual, str) , True)
        self.assertEqual(isinstance(actual, int), False)

    def test_scrapper_number_items(self):
        with open('indexWoolies.html') as html:
            container_soup = soup(html, 'html.parser')

        container_soup = container_soup.findAll('div', {'class': 'shelfProductTile-information'})
        arr, n_items = scrapping(container_soup, 'Fruits&Veg')

        self.assertEqual(n_items, 4)

    def test_scrapper_name(self):
        with open('indexWoolies.html') as html:
            container_soup = soup(html, 'html.parser')

        container_soup = container_soup.findAll('div', {'class': 'shelfProductTile-information'})
        arr, n_items = scrapping(container_soup, 'Fruits&Veg')

        self.assertEqual(arr[0]["name"], "Red Seedless Watermelon Whole each")

    def test_scrapper_price(self):
        with open('indexWoolies.html') as html:
            container_soup = soup(html, 'html.parser')

        container_soup = container_soup.findAll('div', {'class': 'shelfProductTile-information'})
        arr, n_items = scrapping(container_soup, 'Fruits&Veg')

        self.assertEqual(arr[0]["price"], "$1.90 / 1KG")

    def test_scrapper_category(self):
        with open('indexWoolies.html') as html:
            container_soup = soup(html, 'html.parser')

        container_soup = container_soup.findAll('div', {'class': 'shelfProductTile-information'})
        arr, n_items = scrapping(container_soup, 'Fruits&Veg')

        self.assertEqual(arr[0]["category"], "Fruits&Veg")

    def test_scrapper_availability(self):
        with open('indexWoolies.html') as html:
            container_soup = soup(html, 'html.parser')

        container_soup = container_soup.findAll('div', {'class': 'shelfProductTile-information'})
        arr, n_items = scrapping(container_soup, 'Fruits&Veg')

        self.assertEqual(arr[0]["availability"], True)

if __name__ == "__main__":
    unittest.main()
