# Web Scraper code
import requests
import random
from bs4 import BeautifulSoup
import pandas as pd


# list of user agents to resolve 403 forbidden error
userAgents = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Safari/605.1.1',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.2.1 Safari/605.1.1',
              'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.3 Safari/605.1.1',
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.3',
              'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.3']

# requests
website = "https://hamishandandy.com/shop/"
html_data = requests.get(website, headers={'User-Agent': random.choice(userAgents)})

# Parse HTML Code
# create beautiful soup object
soup = BeautifulSoup(html_data.content, "html.parser")

shop_elements = soup.find_all("div", class_="c-product-tile__wrap")
#print(shop_elements)

# create lists to store product names and 'in stock' information
product_list = []
stock_list = []

# iterate through the shop elements extracting product names and checking if the soldout tag exists
# append this information to the relevant lists
for element in shop_elements:
    product_element = element.find_all("h5")
    stock_element = element.find_all("span", class_="soldout-tag")
    product_text = product_element[0].text
    product_list.append(product_text)
    stock_text = stock_element[0].text if stock_element else "Available"
    stock_list.append(stock_text)

# create dataframe using list information
product_data = pd.DataFrame({"Product": product_list, "In Stock": stock_list})

print(product_data)
