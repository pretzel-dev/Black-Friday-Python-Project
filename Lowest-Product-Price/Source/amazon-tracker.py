from bs4 import BeautifulSoup
import requests
import time

def track(productName):

    get_price = False

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'}
    URL = 'https://www.amazon.com/s?k=' + productName

    while get_price == False:
        page = requests.get(URL, headers=headers)
        beautiful_soup = BeautifulSoup(page.content, 'html.parser')
        prices = []

        spans = beautiful_soup.find_all(class_ = 'a-price-whole')



        for span in spans:
            prices.append(float(span.get_text().replace('.', '').replace(',','')))
            get_price = True

        if(get_price == True):
            print(prices)
        else:
            print("Please wait, this can take a moment...")
        
        time.sleep(1)
    


track('Macbook')
