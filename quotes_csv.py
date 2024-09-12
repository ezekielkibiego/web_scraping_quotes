import requests
from bs4 import BeautifulSoup
import csv

base_url = "https://quotes.toscrape.com/page/{}"


with open("quotes.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author"])
    
    page = 1
    while True:
        url = base_url.format(page)
        response = requests.get(url) # send a Get request to the website
        soup = BeautifulSoup(response.text, "html.parser")
        
        quotes = soup.select(".quote")
        
        if not quotes:
            break

        for quote in quotes:
            text = quote.select_one(".text").get_text()
            author = quote.select_one(".author").get_text()
            # print(f"Quote: {text}\nAuthor: {author}\n") 
            writer.writerow([text, author]) 
            
        page += 1
        
print("All quotes saved to quotes.csv")