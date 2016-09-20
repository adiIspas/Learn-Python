import requests
from bs4 import BeautifulSoup
import webbrowser
import time

def check_site(url):
    urls_founds = []
    current_urls = ["pdf/2016/cazare/Planificare_sedinte_cazare_2016-2017.pdf",
                    "pdf/2016/cazare/ANUNT_CAZARE_2016-2017.pdf",
                    "pdf/2016/cazare/CERERE_CAZARE_2016-2017.pdf",
                    "pdf/2016/cazare/METODOLOGIE_CAZARE_2016-2017.pdf"]

    source_code = requests.get(url)
    plain_text = source_code.text

    soup = BeautifulSoup(plain_text, 'html.parser')

    found = False
    for link in soup.findAll('a'):
        href = link.get('href')

        if href.find('pdf/2016/cazare') is not -1 and href not in current_urls:
            found = True
            urls_founds.append(href)

    if found is True:
        return urls_founds
    else:
        return 0

url = 'http://fmi.unibuc.ro/ro/'

print('Program start on', time.ctime())
print('Now working ...')
while True:
    results = check_site(url)

    if results is not 0:
        print('Site is changed on', time.ctime())

        for new_url in results:
            webbrowser.open(url + new_url)
        break
