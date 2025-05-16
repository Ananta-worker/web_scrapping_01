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

for num, item in enumerate(link_batman, start=1):
    link_head = 'https://subslikescript.com/'
    website = link_head+item
    html = requests.get(website)
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
    nama_file = 'naskah_batman/'+'batman'+str(num)+'.txt'
    file = open(nama_file, mode='w', encoding='utf-8')
    file.write(judul + '\n')
    file.write('-------------------- \n')
    file.write(full_transcript)
    file.close()