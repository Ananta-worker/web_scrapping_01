import requests
from bs4 import BeautifulSoup

website = 'https://subslikescript.com/movie/Superdragon_vs_Superman-72744'
html = requests.get(website)
text_html = html.text

# membuat soup
soup = BeautifulSoup(text_html, 'lxml')

# tag article
box_article = soup.find('article', class_='main-article')

# tag h1
tag_h1 = box_article.find('h1')
judul = tag_h1.getText()

# naskah film
# tag div
tag_div = soup.find('div', class_='full-script')
full_transcrip = tag_div.getText(strip=True, separator='\n')
# print(full_transcrip)
# menyimpan ke dalam txt
file = open('Superman-(1975).txt', mode='w', encoding='utf-8')
# file = open('Superman-(1975).txt', mode='w')
file.write(judul + '\n\n')
file.write(full_transcrip)
file.close()

