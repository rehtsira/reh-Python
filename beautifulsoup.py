import requests
from bs4 import BeautifulSoup

r = requests.get("https://rehtsira.github.io")
print(r.content)
print(r.headers)
print(r.content)
print(r.json)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())

print(soup.title)
print('----')
soup = BeautifulSoup(r.content,"html.parser")

imgs = soup.find_all("a",href=True)
imgs_href = []

for img in imgs:
    imgs_href.append(img['href'])

imgs_set = set(imgs_href)

for img in imgs_set:
    print(img)