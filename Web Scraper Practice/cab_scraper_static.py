# Practice making a web scraper
# Scraping auction data from carsandbids.com

import requests as rq
from bs4 import BeautifulSoup

URL = 'https://carsandbids.com/past-auctions/'
page = rq.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='root')
print(results)

#sold_cars = results.find_all(class_='auction-item')
#print(len(sold_cars))
