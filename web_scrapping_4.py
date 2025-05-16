import requests
from bs4 import BeautifulSoup

try:
    website = 'https://subslikescript.com/movie/Batman_Returns-103776'
    html = requests.get(website)
except Exception:
    None

text_html = html.text

# membuat soup
# judul film
soup = BeautifulSoup(text_html, 'lxml')
box_article = soup.find('article', class_='main-article')
tag_h1 = box_article.find('h1')
judul = tag_h1.getText()

# naskah film
# strip=: menghapus spasi kosong, separator='\n': pisahkan dgn enter
tag_div = box_article.find('div', class_='full-script')
full_transcript = tag_div.getText(strip=True, separator='\n')

# menyimpan ke dalam txt
file = open('batman-1992.txt', mode='w')
file.write(judul + '\n')
file.write('-------------------- \n')
file.write(full_transcript)
file.close()
