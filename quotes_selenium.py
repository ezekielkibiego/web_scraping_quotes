from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

chrome_driver_path = "/usr/local/bin/chromedriver"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.get("https://quotes.toscrape.com/js/")


quotes = driver.find_elements(By.CLASS_NAME, "quote")

for quote in quotes:
    text = quote.find_element(By.CLASS_NAME,"text").text
    author = quote.find_element(By.CLASS_NAME,"author").text
    print(f"Quote: {text}\nAuthor: {author}\n") 
    
driver.quit()