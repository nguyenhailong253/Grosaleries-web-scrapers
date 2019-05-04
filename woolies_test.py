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

    def test_scrapper(self):
        with open('indexWoolies.html') as html:
            container_soup = soup(html, 'html.parser')

        container_soup = container_soup.findAll('div', {'class': 'shelfProductTile-information'})
        arr, n_items = scrapping(container_soup, 'Fruits&Veg')

        self.assertEqual(n_items, 4)

        self.assertEqual(arr[0]["name"], "Red Seedless Watermelon Whole each")
        self.assertEqual(arr[0]["price"], "$1.90 / 1KG")

if __name__ == "__main__":
    unittest.main()
