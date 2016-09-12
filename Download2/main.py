from urllib import request

googUrl = 'http://chart.finance.yahoo.com/table.csv?s=GOOG&a=7&b=12&c=2016&d=8&e=12&f=2016&g=d&ignore=.csv'

def downloadStockData(csvUrl):
    response = request.urlopen(csvUrl)
    csv = response.read()
    csv_str = str(csv)
    lines = csv_str.split("\\n")
    dest_url = r'goog.csv'
    fx = open(dest_url, "w")

    for line in lines:
        fx.write(line + "\n")
    fx.close()

downloadStockData(googUrl)
