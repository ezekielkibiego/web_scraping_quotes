import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/") # send a Get request to the website
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
quotes = soup.select(".quote")
print(quotes)

for quote in quotes:
    text = quote.select_one(".text").get_text()
    # print(text)
    author = quote.select_one(".author").get_text()
    print(f"Quote: {text}\nAuthor: {author}\n")