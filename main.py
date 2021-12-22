# Importing libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen as req

# location
myurl = 'https://www.newegg.com/p/pl?d=graphic+card+video+devices&N=100007709&isdeptsrh=1'

# opening up connection and parsing
html = req(myurl).read()
req(myurl).close()
soup = BeautifulSoup(html, 'html.parser')

# Create a csv
filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping_fees, average_rating\n"
f.write(headers)

# grabs each product
containers = soup.findAll("div", {"class": "item-container"})

for container in containers:
    # brand
    title = container.findAll('div', {"class": "item-info"})
    title = title[0]
    name = title.findAll('a', {"class": "item-brand"})
    brand = name[0].img['title']

    # the name of each product
    product_name = container.img['title']

    # shipping fees
    shipping = container.findAll('li', {"class": "price-ship"})
    price = shipping[0].text

    # rating
    rating = title.findAll('a', {"class": "item-rating"})
    if not rating:
        rating = 'Not Applicable'
    else:
        rating = rating[0].i['aria-label']

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping_fee: " + price)
    print("avg_rating:" + rating)
    f.write(brand + "," + product_name.replace(',', '|') + "," + price + "," + rating + "\n")
f.close()