import requests
from bs4 import BeautifulSoup

response = requests.get("https://quotes.toscrape.com/") # send a Get request to the website
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
quotes = soup.find_all("div", class_="quote")
# print(quotes)

for quote in quotes:
    text = quote.find("span", class_="text").get_text()
    # print(text)
    author = quote.find("small", class_="author").get_text()
    print(f"Quote: {text}\nAuthor: {author}\n")