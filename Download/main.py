import urllib.request
import random

def downloadWebImage(url):
    name = random.randrange(1,100)
    full_name = str(name) + ".jpg"

    urllib.request.urlretrieve(url, full_name)

downloadWebImage("http://wallpapercave.com/wp/JgWwayS.jpg")