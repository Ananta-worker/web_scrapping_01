import requests
from bs4 import BeautifulSoup

try:
    website = 'https://subslikescript.com/search?q=batman'
    html = requests.get(website)
except Exception:
    None

text_html = html.text

# membuat soup
soup = BeautifulSoup(text_html, 'lxml')

# tag_ul
box_ul = soup.find('ul', class_='scripts-list')

# tag_a
tag_a = box_ul.find_all('a')

link_batman = []
for item in tag_a:
    link_batman.append(item['href'])

for item in link_batman:
    link_head = 'https://subslikescript.com/'
    website = link_head+item
    print(website)