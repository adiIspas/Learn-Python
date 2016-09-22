import requests
from bs4 import BeautifulSoup
import webbrowser
import time


def check_site(url, number_urls):
    source_code = requests.get(url)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text, 'html.parser')

    found = False
    current_number_urls = 0
    for link in soup.findAll('a'):
        current_number_urls += 1

    if current_number_urls != number_urls:
        found = True

    if found is True:
        return 1
    else:
        return 0

base_url = 'http://fmi.unibuc.ro/ro/'

print('Program start on', time.ctime())
print('Now working ...')
while True:
    results = check_site(base_url, 88)

    if results is not 0:
        print('Site is changed on', time.ctime())
        webbrowser.open(base_url)
        break
