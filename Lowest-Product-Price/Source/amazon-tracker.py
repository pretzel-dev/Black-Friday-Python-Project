from bs4 import BeautifulSoup
import requests

def track(productName):
    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'}
    URL = 'https://www.amazon.com/s?k=' + productName
    page = requests.get(URL, headers=headers)
    beautiful_soup = BeautifulSoup(page.content, 'html.parser')
    prices = []

    spans = beautiful_soup.find_all('span', {'class': 'a-price-whole'})

    for span in spans:
        prices.append(span.get_text())
    
    print(prices)



track('Macbook')
