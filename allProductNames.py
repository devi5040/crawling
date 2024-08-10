# The code illustrates the process of getting all products name from a cateory page
from bs4 import BeautifulSoup
import requests


umniahUrl = "https://eshop.umniah.com/en/devices/handsets.html"
response = requests.get(umniahUrl)
umniahData = response.text
umniahSoup = BeautifulSoup(umniahData, 'html.parser')
pNames = umniahSoup.find_all('a', {'class': 'product-item-link'})
for pName in pNames:
    print(pName.text)
