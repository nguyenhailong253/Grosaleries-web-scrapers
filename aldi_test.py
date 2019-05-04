import unittest
import datetime
from bs4 import BeautifulSoup as soup
from Aldihelper import *

class TestAldi(unittest.TestCase):

    def test_converter(self):
        obj = datetime.datetime.now()
        actual = myconverter(obj)
        
        self.assertEqual(isinstance(actual, str) , True)
        self.assertEqual(isinstance(actual, int), False)

    def test_scrapper(self):
        with open('indexAldi.html') as html:
            container_soup = soup(html, 'html.parser')

        container_soup = container_soup.findAll('a', {'title': 'to product detail'})
        arr, n_items = scrapping(container_soup, 'Snacks')

        self.assertEqual(n_items, 5)

        self.assertEqual(arr[0]["name"], "Berg Maple Streaky Bacon 200g")
        self.assertEqual(arr[0]["price"], "$19.95 per kg")

if __name__ == "__main__":
    unittest.main()
