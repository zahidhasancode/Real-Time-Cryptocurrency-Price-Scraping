import requests
from bs4 import BeautifulSoup
import time

def get_agc_price():
    url = 'https://www.coinscan.com/tokens/matic/0x8837a61644d523cbe5216dde226f8f85e3aa9be3'
    
    # Fetch the webpage
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve data")
        return None

    # Parse the webpage
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Navigate through the nested classes to find the specific price element
    parent_element = soup.find('div', class_='asset-price-chip-wrap e6kb1164 css-13z0f4w ex9mc380')
    
    if parent_element:
        price_element = parent_element.find('span', class_="price-container css-1bmnxg7 e67nlw31")
        if price_element:
            return price_element.text
        else:
            print("Price element not found within specified parent")
            return None
    else:
        print("Parent element not found")
        return None

# Repeat the function every 5 seconds
while True:
    price = get_agc_price()
    if price:
        print(f"Current AGC Price: {price}")
    else:
        print("Unable to fetch the price.")
    time.sleep(5)
