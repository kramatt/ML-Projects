# Practice making a web scraper
# Scraping auction data from bringatrailer.com

import requests as rq
from bs4 import BeautifulSoup

URL = 'https://bringatrailer.com/auctions/results/'
page = rq.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

#results = soup.find(class_='site-content').find(class_='auction-results').find(class_='blocks')
#print(results)

results = soup.find('div', class_='auction-results').find('div', class_='overlayable').find('div', class_='blocks')
print(results)

past_auctions = results.find_all('div', class_='block')
print('past auctions:',past_auctions)
for auction in past_auctions:
    title_elem = auction.find('h3', class_='title')
    subtitle_elem = auction.find('div', class_='subtitle')
    if None in (title_elem, subtitle_elem):
        continue
    print(title_elem.text.strip())
    print(subtitle_elem.text.strip())
    print()
