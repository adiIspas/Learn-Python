import requests
from bs4 import BeautifulSoup
import webbrowser
import time

def check_site(url, number_urls):
    urls = 0
    source_code = requests.get(url)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text, 'html.parser')

    for link in soup.findAll('a'):
        href = link.get('href')

        if href.find('pdf/2016/cazare') is not -1:
            urls += 1

    if urls > number_urls:
        return 1
    else:
        return 0

url = 'http://fmi.unibuc.ro/ro/'
number_urls = 4

print('Program start on', time.ctime())
print('Now working ...')
while True:
    result = check_site(url, number_urls)

    if result is 1:
        print('Site is changed on', time.ctime())
        webbrowser.open(url)
        break
