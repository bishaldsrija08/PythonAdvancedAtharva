# API to fetch product data and display prices
import requests

api_url = "https://690f18d6bd0fefc30a06b965.mockapi.io/product/"

response = requests.get(api_url)

if response.status_code == 200:
    products = response.json()
    for product in products:
        print(f"The price of {product["product"]} is {product["price"]}.")
else:
    print("Failed to retrieve products.")