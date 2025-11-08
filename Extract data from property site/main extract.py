import requests
from bs4 import BeautifulSoup


response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
response.raise_for_status()

soup = BeautifulSoup()
soup.get(response.text, "html.parser")


soup.find("data-test")
print(soup)