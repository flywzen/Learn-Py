import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/catalogue/category/books_1/index.html"

try:
    response = requests.get(url)
    response.raise_for_status()  # Check if the request was successful
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract product names
    products = soup.find_all("h3")
    for product in products:
        print(product.find("a")["title"])
except requests.exceptions.RequestException as e:
    print(f"Error fetching the URL: {e}")