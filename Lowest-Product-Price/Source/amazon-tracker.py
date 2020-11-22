from bs4 import BeautifulSoup
import requests
import time

def track(productName):

    ready = False

    headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0'}
    URL = 'https://www.amazon.com/s?k=' + productName

    while ready == False:  
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        products = []
        elements = soup.find_all('div', attrs={'data-component-type':'s-search-result'})

        for element in elements:
            try:
                title = element.find('span', class_='a-size-medium a-color-base a-text-normal').getText()
                price = float(element.find('span', class_='a-price-whole').get_text().replace(',', '').replace('.', ''))
                products.append([title, price])
                ready = True
            except:
                ready = False
        
    if(ready == True):
        print('All prices:')
        for i in range(len(products)):
            print(products[i])
        
        print('\n\n\n\n')
        print(cheapest_products(products, productName))

def cheapest_products(products, key):
    cheapest_product = []
    key_list = key.split(' ')
    key_targetting = 0
    for i in range(len(products)):
        if cheapest_product != [] and cheapest_product[1] > products[i][1]:
            for x in range(len(key_list)):
                if(key_list[x] in products[i][0]):
                    key_targetting += 1
            
            if(key_targetting >= 0.8*len(key_list)):
                cheapest_product = products[i]
        elif cheapest_product == []:
            cheapest_product = products[i]
        continue
    if(cheapest_products != []):
        return(cheapest_product)
    else:
        track(key)




track('55 inch tv')
