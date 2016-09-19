import urllib.request

def read_text():
    quotes = open("E:\Learn-Python\Check errors\movie_quotes.txt")
    contents_of_file = quotes.read()
    quotes.close()
    check_errors(contents_of_file)


def check_errors(text):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + "shot")
    output = connection.read()
    connection.close()

    if "true" in str(output):
        print("Alert, errors!")
    elif "false" in str(output):
        print("No errors")
    else:
        print("I don't read the text")

read_text()

