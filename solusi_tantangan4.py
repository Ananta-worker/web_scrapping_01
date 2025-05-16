import requests
from bs4 import BeautifulSoup

website = 'https://subslikescript.com/search?q=superman'
html = requests.get(website)
text_html = html.text

# membuat soup
soup = BeautifulSoup(text_html, 'lxml')

# tag ul
box_ul = soup.find('ul', class_='scripts-list')

# tag a
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
    soup = BeautifulSoup(text_html, 'lxml')

    box_article = soup.find('article', class_='main-article')

    # judul film
    tag_h1 = box_article.find('h1')
    judul = tag_h1.getText()

    # naskah film
    tag_div = box_article.find('div', class_='full-script')
    full_transcript = tag_div.getText(strip=True, separator='\n')

    # menyimpan ke dalam text
    nama_file = 'naskah_superman/'+'superman'+str(num)+'.txt'
    file = open(nama_file, mode='w', encoding='utf-8')
    file.write(judul + '\n\n')
    file.write(full_transcript)
    file.close()