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

    def test_scrapper_number_items(self):
        with open('indexAldi.html') as html:
            container_soup = soup(html, 'html.parser')

        container_soup = container_soup.findAll('a', {'title': 'to product detail'})
        arr, n_items = scrapping(container_soup, 'Snacks')

        self.assertEqual(n_items, 5)

    def test_scrapper_name(self):
        with open('indexAldi.html') as html:
            container_soup = soup(html, 'html.parser')

        container_soup = container_soup.findAll('a', {'title': 'to product detail'})
        arr, n_items = scrapping(container_soup, 'Snacks')

        self.assertEqual(arr[0]["name"], "Berg Maple Streaky Bacon 200g")

    def test_scrapper_price(self):
        with open('indexAldi.html') as html:
            container_soup = soup(html, 'html.parser')

        container_soup = container_soup.findAll('a', {'title': 'to product detail'})
        arr, n_items = scrapping(container_soup, 'Snacks')

        self.assertEqual(arr[0]["price"], "$19.95 per kg")

    def test_scrapper_category(self):
        with open('indexAldi.html') as html:
            container_soup = soup(html, 'html.parser')

        container_soup = container_soup.findAll('a', {'title': 'to product detail'})
        arr, n_items = scrapping(container_soup, 'Stationery')

        self.assertEqual(arr[0]["category"], "Stationery")

    def test_scrapper_availability(self):
        with open('indexAldi.html') as html:
            container_soup = soup(html, 'html.parser')

        container_soup = container_soup.findAll('a', {'title': 'to product detail'})
        arr, n_items = scrapping(container_soup, 'Stationery')

        self.assertEqual(arr[0]["availability"], True)

    def test_scrapper_piclink(self):
        with open('indexAldi.html') as html:
            container_soup = soup(html, 'html.parser')

        container_soup = container_soup.findAll('a', {'title': 'to product detail'})
        arr, n_items = scrapping(container_soup, 'Stationery')

        self.assertEqual(arr[0]["pic"], "https://www.aldi.com.au/fileadmin/fm-dam/Products/Groceries/Super_Savers/2019/Produce/Weekly/WK19/W19_SUPER_SAVERS_MEAT_1x1_.jpg")

if __name__ == "__main__":
    unittest.main()
