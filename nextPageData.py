# Code is for extracting the data from next page link

from bs4 import BeautifulSoup
import requests
umniahUrl = "https://dpbooks.in/collections/anuvaadit-kthaa-kaadnbrii?page=1"
job = 0
p_no = 1
while True:
    response = requests.get(umniahUrl)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')
    tags = soup.find_all('div', {'class': 'grid-view-item product-card'})
    for tag in tags:
        job += 1
        title = tag.find(
            'div', {'class': 'h4 grid-view-item__title product-card__title'})
        price = tag.find('span', {'class': 'price-item price-item--sale'})
        print("Title : ", title.text)
        print("Price : ", price.text)
    url_tag = soup.find('a', {'class': 'btn btn--tertiary btn--narrow'})
    if url_tag.get('href') and p_no <= 5:
        p_no += 1
        umniahUrl = 'https://dpbooks.in/collections/anuvaadit-kthaa-kaadnbrii?page=' + \
            str(p_no)
        print('Url:', umniahUrl)
    else:
        break
print('Job :', job)
