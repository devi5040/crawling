from bs4 import BeautifulSoup
import requests

url = "https://www.umniah.com/about_us/"
response = requests.get(url)

data = response.text

soup = BeautifulSoup(data, 'html.parser')
print(soup)
