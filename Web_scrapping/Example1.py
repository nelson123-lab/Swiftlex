import requests
from bs4 import BeautifulSoup

# specify the URL of the website you want to scrape
url = "https://www.example.com/"

# send a GET request to the website
response = requests.get(url)

# parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# find the element(s) containing the data you want to scrape
data = soup.find("div", class_="example-class").get_text()

# print the scraped data
print(data)
