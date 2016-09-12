import requests
from bs4 import BeautifulSoup

def trade_spider(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://www.stagiipebune.ro/stagii.html&page_num=' + str(page) + '&page=stagii&domain=4'
        source_code = requests.get(url)
        plain_text = source_code.text

        soup = BeautifulSoup(plain_text, 'html.parser')

        for link in soup.findAll('a',{'class':'item-name'}):
            href = link.get('href')
            print(href)
        page += 1

trade_spider(1)
