# GroSaleries Web Scrapers
Aldi and Woolworths web scrapers.
The scrapers only scrape general information of a product: product name, price, description, date scraped

## About Grosaleries
GroSaleries is a price aggregator for Australian residents looking for cheapest grocery products. User can type in the product name in the search bar and then prices of that product from Woolworths and Aldi will be displayed for user to compare

## Requirements
- Python 3.7.x
- BeautifulSoup4 4.7.1
- urllib3 1.25.2
- Selenium 3.141.0
- unittest 
- ChromeDriver 73.0.3683.68

## Running scraper
Aldi

    cd ./src/aldi
    python aldi.py

Woolies

    cd ./src/woolies
    python woolies.py
