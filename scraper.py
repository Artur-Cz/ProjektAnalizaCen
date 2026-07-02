from bs4 import BeautifulSoup
import requests
import lxml

url = 'https://mapy.geoportal.gov.pl/imapnext/imap/index.html?moduleId=modulRCN&mapview=51.108434%2C17.140649%2C5000s'
webpage = requests.get(url)

soup = BeautifulSoup(webpage.text, 'lxml')
tags = soup.find('div', attrs={'class': 'preloader-dots'})

print(tags.text)