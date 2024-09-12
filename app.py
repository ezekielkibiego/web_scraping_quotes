import requests


response = requests.get("https://quotes.toscrape.com/") # send a Get request to the website
if response.status_code == 200: # Check the status code of the response (200 means OK)
    print("Success!")
    print(response.text) # print the HTML content of the page
    
else:
    print(f"Failed to retieve the page. Status cod: {response.status_code}")